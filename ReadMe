# AI Assistant

A terminal AI assistant I built in Python. It's an upgrade of my earlier
chatbot — this one can save and reload conversations, switch personalities,
and it doesn't crash when something goes wrong.

This is my 7th project. The goal here was to learn some more intermediate
stuff: splitting code into functions, saving data to files, and handling
errors properly instead of letting the program blow up.

## What it can do

- Chat back and forth with memory (it remembers the conversation)
- `/save` — save the current conversation to a file
- `/load` — load a saved conversation back, even in a new session
- `/personality` — switch how the assistant talks (tutor, brainstorm, concise, default)
- `quit` — exit
- If the AI is busy or something fails, it shows a friendly message instead of crashing

## What I used

- Python 3
- google-genai (Google's Gemini API, free tier)

## Things I learned building this

- **Functions** — breaking the code into named, reusable pieces
- **Files + JSON** — saving conversations to disk and reading them back
- **Error handling** — using try/except so the program survives API errors and missing files
- **Dictionaries** — using a lookup table to store the different personalities

## How saving works

Conversations are saved as JSON files in a `conversations/` folder. Saving
writes the conversation list to a file; loading reads it back into memory so
the assistant picks up where it left off.

## Setup

You need a `config.py` file with your own Gemini API key:

    API_KEY = "your-key-here"

`config.py` is gitignored, so the key stays private and isn't in this repo.

## Run it

    python3 assistant.py
    