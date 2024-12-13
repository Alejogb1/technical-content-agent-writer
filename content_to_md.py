import csv
import re
from datetime import datetime
import os
import random
input_csv = 'generated_content.csv'

output_dir = 'md_files'
os.makedirs(output_dir, exist_ok=True)

def generate_slug(title):
    return re.sub(r'[^a-z0-9-]', '', title.lower().replace(" ", "-"))

def generate_id(title):
    return re.sub(r'[^a-z0-9-]', '', title.lower().replace(" ", "-"))

current_date = datetime.now().strftime('%Y-%m-%d')

md_template = """---
title: "{title}"
date: "{date}"
id: "{id}"
---

{content}
"""

with open(input_csv, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        content = row['Content']
        id_value = f"{generate_id(row['Title'])}"

        md_content = md_template.format(
            title=row['Title'],
            date=current_date,
            id=id_value,
            content=content
        )
        
        filename = f"{id_value}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, mode='w', encoding='utf-8') as md_file:
            md_file.write(md_content)
        
        print(f"Processed and saved: {filename}")

print(f"MDX files saved in '{output_dir}' directory.")