"""
CodeAlpha Python Internship -> Task04: Basic Chatbot
A simple rule-based chatbot.

Concepts used: if-elif, functions, loops, input/output.
"""

import string


def clean_input(text):
    """Lowercase the text and remove punctuation so matching is easier."""
    text = text.lower().strip()
    return text.translate(str.maketrans("", "", string.punctuation))


def get_response(user_input):
    """Return the chatbot's reply for the given user message."""
    message = clean_input(user_input)

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message in ("how are you", "how are you doing"):
        return "I'm fine, thanks!"
    elif message in ("what is your name", "whats your name", "who are you"):
        return "I'm CodeAlpha Bot, a simple rule-based chatbot."
    elif message in ("what can you do", "help"):
        return "I can chat about a few things. Try: hello, how are you, what is your name, thanks, or bye."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif message == "":
        return "Say something and I'll reply!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("CodeAlpha Bot: Hi! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("CodeAlpha Bot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()