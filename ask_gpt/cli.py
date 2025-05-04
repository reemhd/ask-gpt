import os
from openai import OpenAI
from dotenv import load_dotenv
from ask_gpt.session import save_session, load_session

load_dotenv()

def main():
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		print("Error: OPENAI_API_KEY not set")
		return

	client = OpenAI(api_key=api_key)

	model = "gpt-4o"

	messages = []

	print(f"ask-gpt | model: {model}")
	print("Type your message or,\nType '\\q' to quit\nType '\\s' to save\nType '\\l' to load\n")

	while True:
		user_input = input("You: ").strip()
		if user_input.startswith("\\"):
			parts = user_input.split()
			command = parts[0]

			if command == "\\q":
				print("Exiting. Goodbye!")
				break

			elif command == "\\s" and len(parts) == 2:
				save_session(messages, parts[1])
				continue

			elif command == "\\l" and len(parts) == 2:
				messages = load_session(parts[1])
				continue

			elif command == "\\c":
				messages = []
				print("Chat history cleared.")
				continue

			else:
				print("Unknown command. Use :save <file>, :load <file>, :exit")
				continue
		
		# Collect user responses
		messages.append({"role": "user", "content": user_input})

		try:
			response = client.chat.completions.create(
				model=model,
				messages=messages
			)
			assistant_reply = response.choices[0].message.content
		except Exception as e:
			print(f"Error during OpenAI request: {e}")
			continue

		# Add gpt responses
		messages.append({"role": "assistant", "content": assistant_reply})
		print(f"GPT: {assistant_reply}\n")
		

if __name__ == "__main__":
	main()