# simply ask GPT
Clone the repo and create a virtual env
bash
```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Copy the example environment file and add your OpenAI API key
```
cp .env.example .env
```

To start chatting
```
python cli.py
```

To quit the chat
```
\q
```

## Features
- Chat directly with OpenAI models
- Maintain conversation history
- Choose different models (coming soon)
- Save chat sessions (coming soon)