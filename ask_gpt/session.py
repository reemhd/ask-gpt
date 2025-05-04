import json
import os
from rich.console import Console

console = Console()

def save_session(messages, filename):
	"""
	Save the chat session to a JSON file.
	"""
	if not filename.endswith(".json"):
		filename += ".json"
	try:
		with open(filename, "w", encoding="utf-8") as f:
			json.dump(messages, f, indent=2, ensure_ascii=False)
		console.print(f"[blue bold]INFO[/blue bold]: Chat saved to {filename}")
	except Exception as e:
		console.print(f"[red bold]ERROR[/red bold]: Failed to save chat: {e}")

def load_session(filename):
	"""
	Load the chat session from a JSON file.
	"""
	if not filename.endswith(".json"):
		filename += ".json"
	if not os.path.exists(filename):
		console.print(f"[red bold]ERROR[/red bold]: File '{filename}' not found.")
		return []
	try:
		with open(filename, "r", encoding="utf-8") as f:
			messages = json.load(f)
		console.print(f"[blue bold]INFO[/blue bold]: Loaded {len(messages)} messages from {filename}")
		return messages
	except Exception as e:
		console.print(f"[red bold]ERROR[/red bold]: Failed to load chat: {e}")
		return []
