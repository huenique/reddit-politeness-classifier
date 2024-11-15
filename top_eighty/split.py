import json
import os

# Load the JSON data
with open('reddit_data.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# Create an output directory
output_dir = "reddit_split_data"
os.makedirs(output_dir, exist_ok=True)

# Iterate over each top-level key in the JSON object
for key, posts in data.items():
    # Count the elements in the current array
    count = len(posts)
    print(f"Key '{key}' has {count} elements.")
    
    # Define the filename for each key
    output_file = os.path.join(output_dir, f"{key}.json")
    
    # Save each key's data to a separate JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(posts, outfile, ensure_ascii=False, indent=2)

print(f"JSON data split into individual files in the '{output_dir}' directory.")
