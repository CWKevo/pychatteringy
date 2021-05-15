from typing import Union, Generator, List

import json
from os import listdir
from random import choice

from pychatteringy.classes.intents import Intent
from pychatteringy.functions.string_operations import are_strings_similar
from pychatteringy.tools.intent_parser import parse_all

from __init__ import ROOT


class ChatBot():
    """
        Initializes a new ChatBot instance.

    ### Parameters:
        - `fallback_response` - Response to return when no intents match.
        - `intents_directory` - Path to your intents directory (without trailing slash). Defaults to `"intents"`.
        - `intent_filename` - File name of intent JSON data to obtain intents from. Defaults to `generic.json"`.
        If omitted, the bot checks for all JSON files in the intents directory.

    ```
        [
            {intent dict},
            {another intent},
        ]
    ```

        - You can minify intents JSON by using the minifier in tools/minifier.py, or by using the `minify_intents()` function in this class.
    """

    def __init__(self, fallback_response: str="Sorry, I don't understand that yet.", intents_directory: str=str(ROOT) + "intents", intent_filename: Union[str, None]=None, threshold: int=65):
        self.fallback = fallback_response
        self.intents_directory = intents_directory
        self.intent_filename = intent_filename
        self.threshold = threshold


    def __intent_generator(self, file: str="generic.json", all_files: Union[bool, None]=None) -> Generator[Intent, None, None]:
        """
            Yields intents from minified intents JSON file.

        ### Parameters:
            - `file` - Intent file to yield from.
            - `all_files` - Yields from all JSON files in `self.intents_directory` instead. `file` is ignored in this case.
            If omitted, this is set based on whether or not `self.intent_filename` is set.
        """

        if all_files != False and self.intent_filename == None:
            all_f = True

        else:
            all_f = False
        
        print(all_f)

        if all_f:
            all_intent_files = [intent_file for intent_file in listdir(self.intents_directory) if intent_file.endswith(".json")]
        else:
            all_intent_files = [file]

        for intent_file in all_intent_files:
            for line in open(f"{self.intents_directory}/{intent_file}", "r", encoding="UTF-8"):
                try:
                    raw = line.strip().rstrip(",") # Remove new lines & trailing "," for json.loads() to work

                    # Skip opening and closing list brackets:
                    if (raw != "[" and raw != "]"):
                        intent_json = json.loads(raw) # type: dict
                        intent = Intent(intent_json)

                        yield intent

                    else:
                        continue

                except:
                    continue


    def __get_possible_intent(self, query: str) -> Union[Intent, None]:
        possible_intents = list() # type: List[Intent]

        for intent in self.__intent_generator():
            for possible_query in intent.user:
                if are_strings_similar(query, possible_query, threshold=self.threshold):
                    if intent not in possible_intents:
                        possible_intents.append(intent)

                else:
                    continue
                    

        highest_priority_intent = max(possible_intents, key=lambda intent: intent.priority)
        return highest_priority_intent


    def get_response(self, query: str) -> str:
        """
            The main function that obtains a response to specific query.
        
        ### Example:
        ```
        chatbot = ChatBot()
        response = chatbot.get_response("Hi!")
        print(response)
        ```
        """
        intent = self.__get_possible_intent(query)

        if not intent:
            return self.fallback

        if intent.conditions.state == True:
            response = choice(intent.bot)

        elif intent.conditions.state == False:
            if intent.conditions.else_responses:
                response = choice(intent.conditions.else_responses)

            else:
                return self.fallback
        else:
            response = choice(intent.bot)

        return response
    

    def parse_intents(self, directory: str=None, output_directory: str=None):
        """
            Converts all intents JSON to a yieldable format.
        """

        in_dir = directory if directory else f"{self.intents_directory}/unparsed"
        out_dir = output_directory if output_directory != None else f"{in_dir}/../"

        return parse_all(directory=in_dir, output_directory=out_dir)
