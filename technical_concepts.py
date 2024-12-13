

import os
import csv
import time
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, GoogleAPICallError

genai.configure(api_key='API KEY')

concepts = [
    "in verilog is it possible to check the conditions of a loop after executing the?",
    "operator in verilog?",
    "generating random numbers in verilog?",
    #...
]

model = genai.GenerativeModel('gemini-2.0-flash-exp')

with open('generated_content.csv', mode='a' if os.path.exists('generated_content.csv') else 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    if file.tell() == 0:
        writer.writerow(['Title', 'Content'])

    start_index = 0
    if os.path.exists('last_processed_index.txt'):
        with open('last_processed_index.txt', 'r') as f:
            start_index = int(f.read().strip())

    for i in range(start_index, len(concepts)):
        concept = concepts[i]
        prompt = (
           f"Without a title and deducing as much as possible from the following question create a 1500 words extended simple personal informal techy tone and little punctuations response You are a tech person who is very experienced in the subject at hand speak in first person and you try write like stackoverflow users do simulate their tone and give fictional details of your past experience with the problem you had with the issue at hand It should be a response with 3 code snippets as examples that should work and instead of links recommend resources like papers or books in the response Also it is another requirement to not use metaphors or fantasy words or analogies of the problem or issue rather use more technical simple stackoverflow-like user language Use only one joke randomly in one part of the response (requirement) But do not use funny words or funny analogies (not allowed) Here is the question: {concept}"
        )

        try:
            response = model.generate_content(prompt)
            generated_text = response.text.strip()
            writer.writerow([concept, generated_text])
            print(f"Processed: {concept}")

            with open('last_processed_index.txt', 'w') as f:
                f.write(str(i + 1))

        except ResourceExhausted:
            print("Quota limit reached. Waiting for 1 minute before continuing...")
            time.sleep(60)  
            continue  

        except GoogleAPICallError as e:
            print(f"Google API call error encountered for concept '{concept}': {e}")
            with open('last_processed_index.txt', 'w') as f:
                f.write(str(i + 1))
            continue

        except Exception as e:
            print(f"An unexpected error occurred for concept '{concept}': {e}")
            with open('last_processed_index.txt', 'w') as f:
                f.write(str(i + 1))
            continue

print("Content generation completed. Results saved to 'generated_content.csv'.")