# Libraries

import openai
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Prompting

PROMPT = """
        You will receive the draft content of a blog as text. Your task is to generate a proofread version of the file.

        As output, you are required to provide the following:

        1. Orthography Revision: Identify errors and provide their corrections.
        2. Grammatical Revision: Highlight areas where the text can be improved grammatically and offer better replacements to enhance it.
        3. Structural Revision: Propose an improved paragraph-by-paragraph structure, offering a clearer way to convey the main idea.
        4. Conceptual Revision: Conduct a critical analysis of the entire blog. What are its weaknesses? What ideas can be debated or further explored? Are there debates already covered elsewhere?
        5. Debate Revision: Which sections require deeper exploration? What ideas can be expanded upon?
        6. Suggest Three Title Ideas.
        7. Generate a List of Five Relevant SEO Keywords for the Topic.
        8. Suggest Three Blogs related to the main points discussed in this blog.
        
        Your response should be provided in the following format:
        
        {
            "General review": {
                "Orthography Revision": ["each word missapelled: correction"],
                "Grammatical Revision": ["each sentence that can improve: the improved version"],
                "Structural Revision": "content of structural revision proposing an improved paragraph-by-paragraph structure",
                "Conceptual Revision": "content of conceptual revision conducting a critical analysis of the entire blog. What are its weaknesses? What ideas can be debated or further explored? Are there debates already covered elsewhere?",
                "Debate Revision": "content of debate revision Which sections require deeper exploration? what ideas can be expanded upon?"
            },
            "Titles": {
                "title 1": "first suggested effective title",
                "title 2": "second suggested descriptive title",
                "title 3": "third suggested funny title"
            },
            "SEO": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
            "Blogs regarded": {
                "Blog 1": "Topic of the blog and why it's important",
                "Blog 2": "Topic of the blog and why it's important",
                "Blog 3": "Topic of the blog and why it's important"
            }
        }
        
        """

def proofreading(blog):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [
        {"role":"system", "content":PROMPT}, 
        {"role": "user", "content": f"Please read and improve this blog: {blog}"}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        
    )
    

    try:
        result = json.loads(response.choices[0].message.content)
        return result
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        print("Response content:", response.choices[0].message.content)
        # Handle the error, maybe return an error message or default value
        return {"error": "Invalid JSON response from API."}

@app.route('/proofread', methods=['POST'])
def review():
    blog = request.form['text'] # Add after
    result = proofreading(blog)
    print(result)
    
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)    

    
    