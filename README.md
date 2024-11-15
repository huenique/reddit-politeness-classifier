# Reddit Politeness Classifier

## Overview

This script processes Reddit posts and their comments to analyze **politeness strategies** using OpenAI's GPT models. It focuses on identifying and categorizing the communication strategies employed in both posts and their top 10 comments, providing a structured output that can be used for linguistic, sociological, or psychological research.

The classification is based on **Brown and Levinson's Politeness Theory**, which identifies strategies such as **Positive Politeness**, **Negative Politeness**, **Bald on Record**, and **Off-Record**, along with specific subcategories under each.

### Purpose of the Script

This script was custom-built as part of the study titled **"IDENTIFYING POLITENESS STRATEGIES IN REDDIT FORUMS: A LANGUAGE-BASED STUDY OF USER INTERACTIONS ACROSS DIVERSE SUBREDDIT"**. The study aims to explore how users employ politeness strategies across various subreddits, providing insights into language use in online interactions.

---

## Key Features

- **Automatic Politeness and FTA Classification**: Classifies each post and its top 10 comments into one of the four primary strategies and their subcategories.
- **Efficient Comment Selection**: Processes only the top 10 comments based on their score, reducing computational costs while ensuring relevance.
- **Customizable Output**: Groups data by subreddit and organizes posts and comments under corresponding subreddit names in a JSON file.
- **Cache Support**: Implements caching to avoid re-classifying previously analyzed text, saving time and API tokens.
- **Real-Time Updates**: Continuously updates the JSON output file, enabling real-time monitoring of progress.

---

## Input Requirements

### Directory Structure

The script expects a directory named `reddit_split_data` containing JSON files, each named after a subreddit (e.g., `LegalAdvice.json`). Each JSON file should follow this format:

```json
[
  {
    "title": "Post Title Here",
    "selftext": "Optional post body text.",
    "score": 123,
    "url": "https://example.com/post-link",
    "num_comments": 45,
    "created_utc": 1672531199,
    "comments": [
      {
        "comment_id": "c1",
        "comment_body": "Example comment text.",
        "comment_score": 10,
        "comment_created_utc": 1672531200
      }
    ]
  }
]
```

### API Key

You must set your OpenAI API key in the script. Replace `"YOUR_API_KEY"` with your valid OpenAI API key.

---

## Output Format

The script generates a JSON file named `tagged_reddit_data.json` in the following format:

```json
{
  "LegalAdvice": {
    "posts": [
      {
        "post_id": "p1",
        "title": "Stolen car been sold to a person, now he want me to pay him after car been recovered.",
        "politeness_tag": {
          "strategy": "Bald On Record",
          "subcategory": "Unknown"
        },
        "comments": [
          {
            "comment_id": "c1",
            "comment_body": "Only the District Attorney can charge you with a crime.",
            "politeness_tag": {
              "strategy": "Negative Politeness",
              "subcategory": "Giving deference"
            }
          }
        ]
      }
    ]
  }
}
```

---

## Installation and Setup

### Prerequisites

- Python 3.10+
- OpenAI Python SDK (`openai`)
- A valid OpenAI API key

### Install Dependencies

Run the following command to install required libraries:

```bash
pip install openai
```

### Directory Structure Setup

Ensure that the `reddit_split_data` directory exists and contains properly formatted JSON files.

---

## How to Run

1. Place the input JSON files in the `reddit_split_data` directory.
2. Open the script and replace `YOUR_API_KEY` with your OpenAI API key.
3. Run the script:

    ```bash
    python script_name.py
    ```

4. Monitor progress:
   - Logs are written to `classification.log`.
   - The output file `tagged_reddit_data.json` is continuously updated.

---

## Methodology

1. **Input Parsing**:
   - The script reads all JSON files in the `reddit_split_data` directory.
   - Each file corresponds to a subreddit and contains posts with comments.

2. **Politeness Classification**:
   - For each post, the script classifies the title using OpenAI's GPT model.
   - For comments, it sorts by score in descending order and selects the top 10 for classification.

3. **Output Formatting**:
   - Results are stored in a JSON file where each subreddit is a root key.
   - Posts and their comments are nested under the `"posts"` list for the respective subreddit.

4. **Caching**:
   - Previously classified posts and comments are cached to reduce duplicate API calls.

---

## Customization

### Changing the Number of Comments

To classify more or fewer than 10 comments, modify this line in the script:

```python
sorted_comments = sorted(post.get("comments", []), key=lambda x: x.get("comment_score", 0), reverse=True)[:10]
```

Replace `10` with your desired number of comments.

---

## Limitations

- **API Costs**: The script relies on OpenAI's GPT model, which incurs usage costs.
- **Data Quality**: Input JSON files must be properly formatted. Malformed data will cause errors.
- **Response Consistency**: The classifier relies on the model's ability to consistently identify strategies and subcategories. Unexpected model behavior may require manual review.

---

## Acknowledgments

This script was custom-built for the study **"IDENTIFYING POLITENESS STRATEGIES IN REDDIT FORUMS: A LANGUAGE-BASED STUDY OF USER INTERACTIONS ACROSS DIVERSE SUBREDDIT"**. The research leverages OpenAI's cutting-edge GPT models and builds on **Brown and Levinson's Politeness Theory**, providing a detailed analysis of politeness strategies in online discourse.

---

## License

This script is open-source and available for academic and research use. Attribution is appreciated.
