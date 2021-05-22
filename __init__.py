import sys
from pathlib import Path

ROOT = Path(__file__).parent.absolute()
sys.path.append(ROOT)

TEST_CONTEXTS = True

from pychatteringy.classes.chatbot import ChatBot


if __name__ == "__main__":
    chatbot = ChatBot(intent_file="context_test.json", intents_directory=f"{ROOT}/pychatteringy/data/intents", user_data_directory=f"{ROOT}/pychatteringy/data/users")

    while True:
        x = chatbot.chat(input(f"{chatbot.user}: "))
        print("Clyde:", x)
