import json

import praw

# Configure Reddit API credentials
reddit = praw.Reddit(
    client_id="gYPHV_b01S2xmDX7N41xmA",  # Replace with your client_id
    client_secret="W0Kc0Kyz8VpT4V68Vx_ZfLqGwxk6sg",  # Replace with your client_secret
    user_agent="Top80Scraper by /u/hju-fl",  # Replace with your user agent
    username="hju-fl",
    password="myhju213"
)

subreddits = [
    "LegalAdvice", "ChangeMyView", "TooAfraidToAsk", 
    "ExplainLikeImFive", "Awww", "gaming", "books", "relationshipAdvice"
]

data = {}

for subreddit_name in subreddits:
    print(f"Scraping r/{subreddit_name}...")
    subreddit = reddit.subreddit(subreddit_name)
    
    # Retrieve top 80 hot posts
    posts = []
    for post in subreddit.hot(limit=10):
        post_info = {
            "title": post.title,
            "selftext": post.selftext,  # Add the OP's body text
            "score": post.score,
            "url": post.url,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "comments": []
        }
        
        # Fetch all comments
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            post_info["comments"].append({
                "comment_id": comment.id,
                "comment_body": comment.body,
                "comment_score": comment.score,
                "comment_created_utc": comment.created_utc
            })
        
        posts.append(post_info)
    
    data[subreddit_name] = posts

# Save to JSON file
with open("reddit_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Scraping complete. Data saved to reddit_data.json")
