import json
from os import listdir


def parse_all(directory: str="intents/unparsed", output_directory: str="intents"):
    for file in listdir(directory):
        minified_file = open(f"{output_directory}/{file}", "w")

        if file.endswith(".json"):
            with open(f"{directory}/{file}", "r") as unminified_file:
                l = json.load(unminified_file) # type: list

                if not type(l) == list:
                    raise TypeError("Intent JSON must be a list.")

                minified_file.write("[\n")

                for intent_dict in l:
                    minified = json.dumps(intent_dict)
                    minified_file.write(f"  {minified}{',' if intent_dict != l[-1] else ''}\n")

                minified_file.write("]\n")

        else:
            continue


if __name__ == "__main__":
    parse_all()
