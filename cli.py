# cli.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not set")
        return

    client = OpenAI(api_key=api_key)

    model = "gpt-4o"

    print(f"Using model: {model}")
    print("Type your message (or type ':exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.strip() == ":exit":
            print("Exiting...")
            break

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "developer", "content": user_input}]
        )

        assistant_reply = response.choices[0].message.content
        print(f"GPT: {assistant_reply}\n")

if __name__ == "__main__":
    main()