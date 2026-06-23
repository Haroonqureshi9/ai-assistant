from google import genai
from config import API_KEY
import json
import os

client = genai.Client(api_key=API_KEY)


def get_ai_response(conversation):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation
    )
    return response.text


def save_conversation(conversation, filename):
    os.makedirs("conversations", exist_ok=True)
    path = "conversations/" + filename + ".json"
    with open(path, "w") as f:
        json.dump(conversation, f, indent=2)
    print("Saved to", path)


def chat():
    print("Welcome to Chatbot! Type quit to exit, or /save to save.")
    conversation = []

    while True:
        user_message = input("\nYou: ").strip()

        if user_message == "quit":
            print("Goodbye!")
            break

        if user_message == "/save":
            name = input("Save as (name): ")
            save_conversation(conversation, name)
            continue
        if user_message == "":
            continue

        conversation.append({"role": "user", "parts": [{"text": user_message}]})

        reply = get_ai_response(conversation)
        print("Gemini:", reply)

        conversation.append({"role": "model", "parts": [{"text": reply}]})


chat()