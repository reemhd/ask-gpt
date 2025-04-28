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

    messages = []

    print(f"Using model: {model}")
    print("Type your message (or type '\q' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "\q":
            print("Exiting...")
            print("Thanks for using ask-gpt")
            break
        
        # Collect user responses
        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )
            assistant_reply = response.choices[0].message.content
            # Add gpt responses
            messages.append({"role": "assistant", "content": assistant_reply})
            print(f"GPT: {assistant_reply}\n")
        except Exception as e:
            print(f"Error during OpenAI request: {e}")
            continue
        

if __name__ == "__main__":
    main()