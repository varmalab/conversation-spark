# Build 2025 Conversation Openers AI Helper

A playful chat app built with [GitHub Models](https://docs.github.com/en/github-models) to help you spark better conversations at Microsoft Build.

Just describe something about a person — their shirt, job, or vibe — and get a thoughtful, funny, or curious question you can ask to break the ice. It's a conversation helper for hallway chats, coffee lines, and awkward silences.

## 🚀 Try it live

👉 \[Insert live demo link here]

## 🛠 How it works

* Built using Python (Flask/FastAPI) with a simple HTML frontend
* Calls the [GitHub Models API](https://docs.github.com/en/github-models) under the hood
* You input a short phrase (e.g. *"they're wearing a NASA shirt"*)
* The model returns a natural-sounding question you can ask that person

## 🧪 Sample inputs

> “They mentioned they work in AI policy.”
> → *"What’s something about AI policy that most people get totally wrong?"*

> “He’s holding a very colorful coffee cup.”
> → *"Is there a story behind that cup? It looks like it has a personality."*

> “Wearing a Dungeons & Dragons shirt.”
> → *"Are you the dungeon master, or just a very committed party member?"*

## 🔧 Running locally

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/build-2025-conversation-openers.git
cd build-2025-conversation-openers

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and set your GitHub Models token
echo "GITHUB_TOKEN=your_token_here" > .env

# Run the app
python app.py

```
Then open http://localhost:8000 in your browser.


## ✨ Built with

* [GitHub Models](https://docs.github.com/en/github-models)
* Python (Flask or FastAPI)
* Azure AI SDK for inference

## 💬 Made by

Built by [@katecatlin](https://github.com/katecatlin) and [@damovisa](https://github.com/damovisa) for Microsoft Build 2025. Enjoy it, remix it, and talk to strangers better ✨

