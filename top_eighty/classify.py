import json
import logging
import os
import re
from typing import Any, Dict, List, Tuple, Union

from openai import OpenAI

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("classification.log"), logging.StreamHandler()],
)

# ANSI escape codes for coloring
COLOR_GREEN = "\033[92m"  # Green
COLOR_RED = "\033[91m"  # Red
COLOR_RESET = "\033[0m"  # Reset color to default

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define data structures
CommentData = Dict[str, Union[str, int, float]]
PolitenessTag = Dict[str, Union[str, None]]
PostData = Dict[str, Union[str, PolitenessTag, List[CommentData]]]

# Define the directory containing the JSON files and the output file
data_directory: str = "reddit_split_data"
output_file: str = "tagged_reddit_data.json"

# Cache for previously analyzed posts and comments
comment_cache: Dict[str, PolitenessTag] = {}

# Load cache from a file if it exists
cache_file: str = "comment_cache.json"
if os.path.exists(cache_file):
    with open(cache_file, "r") as cache_f:
        comment_cache = json.load(cache_f)
    logging.info("Loaded comment cache from file.")
else:
    logging.info("No cache file found. Starting with an empty cache.")

# Step 1: Initialize the output JSON file with all root keys
subreddit_names = [
    os.path.splitext(filename)[0]
    for filename in os.listdir(data_directory)
    if filename.endswith(".json")
]
initial_data: Dict[str, Dict[str, List[Any]]] = {
    name: {"posts": []} for name in subreddit_names
}

# Write the initial structure to the output file
with open(output_file, "w") as f:
    json.dump(initial_data, f, indent=4)

logging.info(f"Initialized {output_file} with root keys for each subreddit.")


# Function to classify text for politeness strategies and FTAs
def classify_text(text: Any, is_post: bool = True) -> PolitenessTag:
    if text in comment_cache:
        logging.debug(f"Cache hit for text: {text}")
        return comment_cache[text]

    logging.info(f"Classifying {'post title' if is_post else 'comment'}: {text}")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a classifier for politeness strategies and face-threatening acts.",
                },
                {
                    "role": "user",
                    "content": f"Classify the {'post title' if is_post else 'comment'}: '{text}' and identify both the main strategy (Positive Politeness, Negative Politeness, Bald on Record, Off-Record) and its specific subcategory.",
                },
            ],
            max_tokens=50,
        )

        # assert that response.choices[0].message.content is not None
        assert response.choices[0].message.content is not None
        response_text = response.choices[0].message.content.strip()
        strategy, subcategory = parse_response(response_text)

        tag: PolitenessTag = {"strategy": strategy, "subcategory": subcategory}
        comment_cache[str(text)] = tag

        color = COLOR_GREEN if strategy != "Unknown" else COLOR_RED
        logging.info(
            f"{color}Classification result: {{'strategy': '{strategy}', 'subcategory': '{subcategory}'}}{COLOR_RESET}"
        )
        return tag

    except Exception as e:
        logging.error(f"Error classifying text: {e}")
        return {"strategy": "Error", "subcategory": None}


# Helper function to parse response and extract strategy and subcategory
def parse_response(response_text: str) -> Tuple[str, str]:
    strategy = "Unknown"
    subcategory = "Unknown"

    strategy_pattern = (
        r"(Positive Politeness|Negative Politeness|Bald on Record|Off-Record)"
    )
    subcategory_patterns = {
        "Positive Politeness": r"(Lighthearted remarks|Compliments|Jokes|In-group jargon|Tag questions|Honorifics|Nicknames|Discourse markers)",
        "Negative Politeness": r"(Questioning|Hedging|Conveying disagreements|Seeking favor|Apologizing|Pessimistic remarks|Conveying difference|Giving orders)",
        "Bald on Record": r"(Imperative forms|Direct remarks|Concise|Clear|Commands)",
        "Off-Record": r"(Indirect|Expresses something in a broad sense|Saying things differently)",
    }

    strategy_match = re.search(strategy_pattern, response_text, re.IGNORECASE)
    if strategy_match:
        strategy = strategy_match.group(0).title()

    if strategy in subcategory_patterns:
        subcategory_match = re.search(
            subcategory_patterns[strategy], response_text, re.IGNORECASE
        )
        if subcategory_match:
            subcategory = subcategory_match.group(0).title()

    return strategy, subcategory


# Step 2: Process each JSON file and append posts to the initialized structure
for filename in os.listdir(data_directory):
    if filename.endswith(".json"):
        root_key = os.path.splitext(filename)[
            0
        ]  # Derive root key from filename (e.g., "LegalAdvice")

        file_path = os.path.join(data_directory, filename)
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            logging.info(f"Loaded data from {filename}")
        except Exception as e:
            logging.error(f"Error loading JSON from {filename}: {e}")
            continue

        # Append posts for the current file's subreddit
        for post in data:
            post_title = post.get("title", "")
            post_tag = classify_text(post_title, is_post=True)

            # Sort comments by score and take the top 10
            sorted_comments = sorted(
                post.get("comments", []),
                key=lambda x: x.get("comment_score", 0),
                reverse=True,
            )[:10]

            comments: list[Any] = []
            for comment in sorted_comments:
                comment_body = comment.get("comment_body", "")
                comment_tag = classify_text(comment_body, is_post=False)
                comments.append(
                    {
                        "comment_id": comment.get("comment_id", ""),
                        "comment_body": comment_body,
                        "politeness_tag": comment_tag,
                    }
                )

            # Load existing data, append the new post, and save
            with open(output_file, "r+") as f:
                file_data = json.load(f)
                file_data[root_key]["posts"].append(
                    {
                        "post_id": post.get("post_id", ""),
                        "title": post_title,
                        "politeness_tag": post_tag,
                        "comments": comments,
                    }
                )
                f.seek(0)
                json.dump(file_data, f, indent=4)

logging.info(f"Updated tagged data saved to {output_file}")

# Save the cache to a file at the end of processing
with open(cache_file, "w") as cache_f:
    json.dump(comment_cache, cache_f, indent=4)

logging.info("Comment cache saved to file.")
