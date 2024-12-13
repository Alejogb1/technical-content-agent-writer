
## Usage

### Install the required Python libraries:

```pip install google-generativeai```


Set up the API key:

Replace API KEY in the script with your Google Generative AI API key.

Ensure required folders exist:

	•	generated_content.csv will be created automatically if not present.
	•	md_files directory will be created for storing Markdown files.

Content Generation

Run the first script to generate responses:

```python content_generator.py```

This AI Technical Agent is a Python-based tool designed to generate detailed technical responses to specific user-defined questions or concepts, leveraging Google Generative AI’s Gemini-2.0 model. The agent provides StackOverflow-style responses, including working code examples and suggested technical resources, while maintaining an informal yet tech-oriented tone. It automates the process of content generation, saves the results in a CSV file, and further converts the generated responses into Markdown files for structured documentation.

Features

Automated Content Generation:

	•	Uses Google Generative AI’s Gemini-2.0 model to generate 1500-word responses to user-defined technical questions.
	•	Outputs responses in a personal, informal, and technical tone, similar to StackOverflow.
 
Error Handling and Resumption:

	•	Handles API quota limits and other exceptions gracefully.
	•	Saves progress to a file (last_processed_index.txt) to resume from the last processed question.
 
CSV Storage:

	•	Stores generated responses in a CSV file (generated_content.csv) with fields for titles and content.
 
Markdown Conversion:

	•	Converts CSV entries into Markdown files using a predefined template for further use in documentation or static site generation.
	•	Saves Markdown files in a structured folder (md_files).
 
ID and Slug Generation:

	•	Generates SEO-friendly slugs and unique IDs for each Markdown file based on the title.
 
Configurable and Modular:

	•	Easy to add or update concepts for content generation.
	•	Configurable file paths and templates for customization.

How It Works
1. Add the questions or technical topics you want responses for in the concepts list.

2. The script processes each concept, generates a response using the AI model, and appends it to the generated_content.csv.

3. If the API encounters an issue (e.g., quota limits), the script waits and retries. Progress is saved, ensuring no data is lost.

4. Once content is generated, the second script converts the CSV entries into Markdown files, complete with metadata like title, date, and ID.

Installation

	1.	Clone the repository:

git clone <repository_url>
cd <repository_directory>



Usage

1. Content Generation

Run the first script to generate responses:

python content_generator.py

2. Convert to Markdown

Run the Markdown conversion script:

python csv_to_markdown.py

The Markdown files will be saved in the md_files directory.

File Descriptions

	•	content_generator.py:
	•	Handles question processing, response generation, and CSV storage.
	•	csv_to_markdown.py:
	•	Converts the CSV entries into Markdown files using a pre-defined template.
	•	generated_content.csv:
	•	Stores all generated content in a structured format.
	•	md_files/:
	•	Contains the generated Markdown files, one for each concept.

Example Outputs

CSV Entry

Title,Content
"Generating Random Numbers in Verilog","Here’s how I solved it with three code snippets..."

Markdown File

---
title: "Generating Random Numbers in Verilog"
date: "2024-12-13"
id: "generating-random-numbers-in-verilog"
---

Here’s how I solved it with three code snippets...

Error Handling

	•	Quota Limit:
Waits for 1 minute and retries when the API quota is exhausted.
	•	Unexpected Errors:
Logs the error, saves progress, and continues with the next concept.

Customization

	•	Update the concepts list to include new questions.
	•	Modify the Markdown template in csv_to_markdown.py to fit specific requirements.
	•	Adjust the API key and model configuration for your use case.

Future Enhancements

	•	Add support for more AI models or APIs.
	•	Integrate directly with a static site generator like Hugo or Gatsby.
	•	Extend functionality for real-time updates or webhooks.

License

This project is released under the MIT License. See the LICENSE file for more details.
