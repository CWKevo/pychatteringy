# When you are lonely and you like having conversations with yourself.
# | for multiple possible messages.

import json
from pathlib import Path

intent_template = {
    "user": [],
    "bot": [],
    "priority": 0.5,
    "conditions": {},
    "actions": []
}


def intent_generator(out: str):

    with open(out, "w") as intent_file:

        try:
            intent_file.write("[\n")
            intent = intent_template.copy()

            while True:
                message = input("User says: ")
                intent["user"] = message.split("|")

                message = input("Bot responds with: ")
                intent["bot"] = message.split("|")

                intent_file.write(f"\t{json.dumps(intent)},\n")

        except KeyboardInterrupt:
            intent_file.write("]\n")
            print("\n\nExitting... your JSON should be saved. Just remove the last trailing comma from the intent JSON")
            intent_file.close()


def intent_generator_from_file(from_file: str, output: str):
    out = open(output, "w")

    out.write("[\n")

    intent = intent_template.copy()

    for line in open(from_file, "r"):
        x = line.split("=")
        pair = [y.strip() for y in x]

        if pair[0] == "user":
            intent["user"] = pair[1].split("|")

        elif pair[0] == "bot":
            intent["bot"] = pair[1].split("|")
            out.write(f"\t{json.dumps(intent)},\n")

            intent = intent_template.copy() # re-init/"clear"
            continue

        else:
            continue

    out.write("]\n")
    out.close()
    print("File saved! Don't forget to remove the last trailing comma from the generated JSON.")


def main():
    print(f"""
        Welcome to the intent generator! This CLI tool allows you to quickly create new intents for "pyChatteringy" package.

        You have option to either write messages in terminal directly (1), or import them from a file (2).

        In both cases, you will first be asked for a path to save the intent JSON data into (including filename). If you skip this step,
        then the intent will be saved to "/../../../data/intents/generated.json".

        Option 1 - Write in terminal:
            You will write what user says and what bot responds with in a terminal. It's like having a conversation with yourself. If you wish
            to exit this mode, just hit "Ctrl + C" on your keyboard.
        
        Option 2 - Obtain from file:
            You will be asked for an additional path to a text file of already simulated conversation. The principe is same as the terminal option, but the
            format of the file must be the following:

            {'-' * 35}
            user = user message
            bot = bot response
            user = user message|another possible message
            bot = bot response|another possible response
            # Spaces around "=" are stripped.
            {'-' * 35}
        
            There must never be same message authors twice in a row, eg.:
            
            {'-' * 15}
            user=something
            bot=something
            {'-' * 15}

            Comments are possible, as lines with not "user" or "bot" before "=" are skipped

            If you wish to specify more possible messages, use "|" as a separator.
            For example, writing the following as an user message: "Hi!|Hello!" will cause the bot to react to "Hi!" and "Hello!".
            Writing something like "Good day!|Greetings!" as a bot response will let bot later pick one of the two (or more) messages.
            You can specify as many messages as you like.

            The last trailing comma from the JSON list will not be removed. This is because the entire process is going through a generator, to improve performance
            when handling large data. Here, I sacrificed speed, performance and memory for you to need to remove that comma (when I yield data, I cannot check whether
            or not the element is last in the data).
    """)

    def __choice():
        choice = input("Your choice: ")

        # Terminal:
        if choice.strip() == "1":
            # In:
            output_path = input("Path to the output intent file (existing one will be overwritten!): ")

            if len(output_path) < 1:
                output_path = Path(__file__ + "/../../../data/intents/generated.json")

            # Go:
            intent_generator(output_path)

        # From file:
        elif choice.strip() == "2":
            # In:
            from_file = input("From what file shall I import: ")

            if len(from_file) < 1:
                from_file = Path(__file__ + "/../../../data/intents/unparsed/intents.txt")

            # Out:
            output_path = input("Path to the output intent file (existing one will be overwritten!): ")

            if len(output_path) < 1:
                output_path = Path(__file__ + "/../../../data/intents/generated.json")

            # Go:
            intent_generator_from_file(from_file, output_path)

        else:
            print("Option must be either '1' or '2'.")
            __choice()

    __choice()


if __name__ == "__main__":
    main()
