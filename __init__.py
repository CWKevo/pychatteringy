import sys
from pathlib import Path

ROOT = Path(__file__).parent.absolute()
sys.path.append(ROOT)


from pychatteringy.classes.chatbot import ChatBot


if __name__ == "__main__":
    chatbot = ChatBot()

    while True:
    	x = chatbot.chat(input(f"{chatbot.user}: "))
    	print("Bot:", x)
