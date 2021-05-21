from typing import Union

import json
from pathlib import Path
from os import listdir


def parse_all(directory: Union[str, Path]=Path(__file__ + "/../../data/intents/unparsed"), output_directory: Union[str, Path]=Path(__file__ + "/../../data/intents")):
    for file in listdir(directory):
        if file.endswith(".json"):
            minified_file = open(f"{output_directory}/{file}", "w")

            with open(f"{directory}/{file}", "r") as unminified_file:
                l = json.load(unminified_file) # type: list

                if not type(l) == list:
                    raise TypeError("Intent JSON must be a list.")

                minified_file.write("[\n")

                for intent_dict in l:
                    minified = json.dumps(intent_dict)
                    minified_file.write(f"\t{minified}{',' if intent_dict != l[-1] else ''}\n")

                minified_file.write("]\n")

        else:
            continue


if __name__ == "__main__":
    parse_all()
    print("Successfuly parsed all intents.")
