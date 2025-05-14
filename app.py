from flask import Flask, request, render_template
import os
import yaml  # Add this import
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

app = Flask("Build 2025 Conversation Openers")

# GitHub Models API setup
endpoint = "https://models.github.ai/inference"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Load prompt configuration from .prompt.yml
with open(".prompt.yml", "r") as file:
    prompt_config = yaml.safe_load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    question = None
    if request.method == "POST":
        description = request.form.get("description")
        if description:
            # Prepare messages from the prompt configuration
            messages = [
                {"role": msg["role"], "content": msg["content"].replace("{{input}}", description)}
                for msg in prompt_config["messages"]
            ]
            response = client.complete(
                messages=messages,
                temperature=prompt_config["modelParameters"]["temperature"],
                model=prompt_config["model"]
            )
            question = response.choices[0].message.content
    return render_template("index.html", question=question)

if __name__ == "__main__":
    app.run(debug=True)
