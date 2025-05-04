import os
from openai import OpenAI
from dotenv import load_dotenv
from ask_gpt.session import save_session, load_session
from ask_gpt import system_prompts
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
console = Console()

def main():
	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		console.print("[red bold]Error[/red bold]: OPENAI_API_KEY not set")
		return

	client = OpenAI(api_key=api_key)

	model = "gpt-4o"

	messages = system_prompts.initial_context.copy()

	console.print(f"\n[bold blue]ask-gpt[/bold blue] | [bold yellow]{model}[/bold yellow]\n")
	help_text = """Type your message or,
Type [red]'\\q'[/red] to [bold]quit[/bold]
Type [green]'\\s <filename>'[/green] to [bold]save[/bold]
Type [blue]'\\l <filename>'[/blue] to [bold]load[/bold]
Type [white]'\\c'[/white] to [bold]clear chat history[/bold]
"""
	console.print(help_text)

	while True:
		user_input = console.input("[green bold]You[/green bold]: ").strip()
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
				messages = system_prompts.initial_context.copy()
				print("Chat history cleared.")
				continue

			else:
				console.print(f"Unknown command. {help_text}")
				continue
		
		# Collect user responses
		messages.append({"role": "user", "content": user_input})

		try:
			with console.status("[bold blue]Thinking...[/bold blue]", spinner="dots", spinner_style="blue"):
				# Send the request to OpenAI
				response = client.chat.completions.create(
					model=model,
					messages=messages
				)
			assistant_reply = response.choices[0].message.content
		except Exception as e:
			print(f"[red bold]Error[/red bold] during OpenAI request: {e}")
			continue

		# Add gpt responses
		messages.append({"role": "assistant", "content": assistant_reply})

		# Render markdown
		with console.capture() as capture:
			console.print(Markdown(assistant_reply), markup=True)
		response = capture.get()

		console.print("[blue bold]GPT[/blue bold]: ", end="")
		print(response.strip())
		console.line()

if __name__ == "__main__":
	main()
