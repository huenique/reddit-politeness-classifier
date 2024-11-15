import json
import os

import praw

# Initialize PRAW
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

def extract_reddit_post_and_comments(link, output_file):
    # Get the submission
    submission = reddit.submission(url=link)
    submission.comments.replace_more(limit=None)

    # Extract post data
    post_data = {
        "title": submission.title,
        "author": str(submission.author),
        "selftext": submission.selftext,
        "url": submission.url,
        "score": submission.score,
        "created_utc": submission.created_utc,
        "num_comments": submission.num_comments,
        "comments": []
    }

    # Extract comments
    def parse_comments(comments):
        comment_list = []
        for comment in comments:
            if isinstance(comment, praw.models.Comment):
                comment_list.append({
                    "author": str(comment.author),
                    "body": comment.body,
                    "score": comment.score,
                    "created_utc": comment.created_utc,
                    "replies": parse_comments(comment.replies)
                })
        return comment_list

    post_data["comments"] = parse_comments(submission.comments)

    # Save to JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=4)

# Replace with the Reddit post URL and desired output file name
reddit_post_url = "https://www.reddit.com/r/.../comments/..."
output_file_name = "reddit_post.json"

extract_reddit_post_and_comments(reddit_post_url, output_file_name)
print(f"Reddit post and comments saved to {output_file_name}")
