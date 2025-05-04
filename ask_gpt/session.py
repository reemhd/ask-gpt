import json
import os

def save_session(messages, filename):
	"""
	Save the chat session to a JSON file.
	"""
	if not filename.endswith(".json"):
		filename += ".json"
	try:
		with open(filename, "w", encoding="utf-8") as f:
			json.dump(messages, f, indent=2, ensure_ascii=False)
		print(f"[INFO] Chat saved to {filename}")
	except Exception as e:
		print(f"[ERROR] Failed to save chat: {e}")

def load_session(filename):
	"""
	Load the chat session from a JSON file.
	"""
	if not filename.endswith(".json"):
		filename += ".json"
	if not os.path.exists(filename):
		print(f"[ERROR] File '{filename}' not found.")
		return []
	try:
		with open(filename, "r", encoding="utf-8") as f:
			messages = json.load(f)
		print(f"[INFO] Loaded {len(messages)} messages from {filename}")
		return messages
	except Exception as e:
		print(f"[ERROR] Failed to load chat: {e}")
		return []
