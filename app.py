from flask import Flask, request, render_template
import os
from dotenv import load_dotenv  # Add this import
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()

app = Flask("Build 2025 Conversation Openers")  # Updated app name

# GitHub Models API setup
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

@app.route("/", methods=["GET", "POST"])
def index():
    question = None
    if request.method == "POST":
        description = request.form.get("description")
        if description:
            response = client.complete(
                messages=[
                    SystemMessage("You are an assistant that helps people ask great conversation-starter questions based on what someone looks like or what they’re doing. Respond with one natural-sounding question they could ask."),
                    UserMessage(description),
                ],
                temperature=0.9,
                top_p=1.0,
                model=model
            )
            question = response.choices[0].message.content
    return render_template("index.html", question=question)

if __name__ == "__main__":
    app.run(debug=True)
