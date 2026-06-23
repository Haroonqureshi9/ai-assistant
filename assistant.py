from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

print("Welcome to Chatbot! Type quit to exit.")

conversation = []

while True:
    user_message = input("\nYou: ")
    if user_message == "quit":
        print("Goodbye!")
        break
    conversation.append({"role": "user", "parts": [{"text": user_message}]})
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation
    )
    print("Gemini:", response.text)
    conversation.append({"role": "model", "parts": [{"text": response.text}]})