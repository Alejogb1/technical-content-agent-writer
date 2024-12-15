import csv
import re
from datetime import datetime
import os

# Input and output configurations
input_csv = 'generated_content.csv'
output_dir = 'md_files'
os.makedirs(output_dir, exist_ok=True)

# Function to generate slug
def generate_slug(title):
    return re.sub(r'[^a-z0-9-]', '', title.lower().replace(" ", "-"))

# Function to generate id
def generate_id(title):
    return re.sub(r'[^a-z0-9-]', '', title.lower().replace(" ", "-"))

# Function to sanitize title
def sanitize_title(title):
    # Replace problematic characters with single quotes
    return title.replace('"', "'").replace('[', "'").replace(']', "'")

# Current date in YYYY-MM-DD format
current_date = datetime.now().strftime('%Y-%m-%d')

# Markdown template
md_template = """---
title: "{title}"
date: "{date}"
id: "{id}"
---

{content}
"""

# Read and process the CSV file
with open(input_csv, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # Sanitize the title
        sanitized_title = sanitize_title(row['Title'])
        
        # Generate ID based on sanitized title
        id_value = generate_id(sanitized_title)
        
        # Create Markdown content
        md_content = md_template.format(
            title=sanitized_title,
            date=current_date,
            id=id_value,
            content=row['Content']
        )
        
        # Define the file path and save the file
        filename = f"{id_value}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, mode='w', encoding='utf-8') as md_file:
            md_file.write(md_content)
        
        print(f"Processed and saved: {filename}")

print(f"MDX files saved in '{output_dir}' directory.")
