from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)


def get_ai_response(conversation):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation
    )
    return response.text


def chat():
    print("Welcome to Chatbot! Type quit to exit.")
    conversation = []

    while True:
        user_message = input("\nYou: ")
        if user_message == "quit":
            print("Goodbye!")
            break

        conversation.append({"role": "user", "parts": [{"text": user_message}]})

        reply = get_ai_response(conversation)
        print("Gemini:", reply)

        conversation.append({"role": "model", "parts": [{"text": reply}]})


chat()