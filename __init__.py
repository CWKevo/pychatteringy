import sys
from pathlib import Path

ROOT = Path(__file__).parent.absolute()
sys.path.append(ROOT)


if __name__ == "__main__":
    from pychatteringy.classes.chatbot import ChatBot
    chatbot = ChatBot(intents_directory="intents")

    while True:
    	x = chatbot.get_response(input("You: "))
    	print("Bot:", x)
