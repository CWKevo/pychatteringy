import sys
from pathlib import Path

ROOT = Path(__file__).parent.absolute()
sys.path.append(ROOT)


from pychatteringy.classes.chatbot import ChatBot


if __name__ == "__main__":
    chatbot = ChatBot()

    while True:
    	x = chatbot.chat(__name__, input("You: "))
    	print("Bot:", x)
