from typing import Dict, Iterable, Iterator, Union, Generator, List

import json
from os import listdir
from re import match
from random import choice
from datetime import datetime, time

from pychatteringy.classes.intents import Intent
from pychatteringy.functions.string_operations import strings_similarity
from pychatteringy.tools.intent_parser import parse_all
from pychatteringy.functions.helpers import is_time_between


class ChatBot():
    """
        Initializes a new ChatBot instance.

    ### Parameters:
        - `fallback_response` - Response to return when no intents match.
        - `intents_directory` - Path to your intents directory (without trailing slash). Defaults to `"intents"`.
        - `intent_filename` - File name of intent JSON data to obtain intents from. Defaults to `generic.json"`.
        If omitted, the bot checks for all JSON files in the intents directory.
        - `user_data_directory` - Path to directory (without trailing slash) where user data (sessions) will be saved.
        - `threshold` - Integer tolerance used in intent matching (Levenshtein's scale). Can be from 0 to 100.

    The intent JSON data must look like this:

    ```
        [
            {intent dict},
            {another intent}
        ]
    ```

        - You can parse intents to be in the valid format by using the parser - see `parse_intents()`.
        Note: This is intended for non-huge JSON data. In fact, the only reason why is it parsed like this is because of
        performance reasons. It is easier to yield intents that are oneliners rather than putting entire JSON file in memory (checking for
        brackets accross lines and then yielding valid JSON is pretty tough, so why not make both of our lives easier?)
    """

    def __init__(self, fallback_response: str="Sorry, I don't understand that yet.", threshold: int=65, intents_directory: str="data/intents", intent_file: Union[str, None]=None, user_data_directory: str="data/users"):
        self.fallback = fallback_response
        self.threshold = threshold

        self.intents_directory = intents_directory
        self.intent_filename = intent_file

        self.user_data_directory = user_data_directory

        self.session_cache = dict()


    def __intent_generator(self, file: str="generic.json", all_files: Union[bool, None]=None) -> Generator[Intent, None, None]:
        """
            Yields intents from minified intents JSON file.

        ### Parameters:
            - `file` - Intent file to yield from.
            - `all_files` - Yields from all JSON files in `self.intents_directory` instead. `file` is ignored in this case.
            If omitted, this is set based on whether or not `self.intent_filename` is set.
        """

        if all_files != False and self.intent_filename == None:
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
        possible_intents = list() # type: List[Dict(Intent)]
        same_ratio_intents = list() # type: List[Dict(Intent)]

        for intent in self.__intent_generator(self.intent_filename):
            for possible_query in intent.user:
                ratio = strings_similarity(query, possible_query, threshold=self.threshold)
                if ratio:
                    if intent not in possible_intents:
                        possible_intents.append({ "data": intent, "ratio": ratio })
                else:
                    continue

        if possible_intents:
            highest_ratio_intent = max(possible_intents, key=lambda intent: intent["ratio"])
            same_ratio_intents.append(highest_ratio_intent["data"])

            if same_ratio_intents:
                highest_priority_intent = max(same_ratio_intents, key=lambda intent: intent.priority)

                return highest_priority_intent

            else:
                return None

        else:
            return None


    def update_user_data(self, key, data, user: str) -> dict:
        """
            Updates a key in user data JSON file and returns the new user data.
            Creates the user data file, if necessary.
        """

        def __update():
            try:
                with open(f"{self.user_data_directory}/{user}.json", "r") as raw_user_data:
                    d = raw_user_data.read()

                    if len(d) <= 3:
                        user_data = dict()
                    else:
                        user_data = json.loads(d) # type: dict

            except FileNotFoundError:
                user_data = dict()

            with open(f"{self.user_data_directory}/{user}.json", "w") as raw_user_data:
                user_data[key] = data
                new = json.dumps(user_data)
                raw_user_data.write(new)

                return user_data

        return __update()


    def get_user_data(self, user: str) -> dict:
        """
            Returns user data dictionary from their JSON data file.
        """

        try:
            with open(f"{self.user_data_directory}/{user}.json", "r") as raw_user_data:
                user_data = json.load(raw_user_data)

                return user_data

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return dict()


    def chat(self, user: str, query: str) -> str:
        """
            The main function that obtains a response to specific query.
        
        ### Parameters:
            - `user` - User's name/ID (used to save cache and intent data for the specific user).
            - `query` - Your message for the bot. Intents are matched by Levenshtein's scale.
        
        ### Example:
        ```
        chatbot = ChatBot()
        response = chatbot.chat("clyde", "Hi!")
        print(response)
        ```
        """

        self.update_user_data("last_query", query, user=user)
        intent = self.__get_possible_intent(query)

        if not intent:
            return self.fallback

        response = choice(intent.bot)

        conditions = self.evaluate_intent_conditions(intent.conditions.if_raw, user=user)
        if conditions == False:
            if intent.conditions.else_responses:
                response = choice(intent.conditions.else_responses)
            else:
                return self.fallback

        self.evaluate_intent_actions(user, intent.actions)

        return response


    def parse_intents(self, directory: str=None, output_directory: str=None):
        """
            Converts all intents JSON to a yieldable format.

            This is intended for non-huge JSON data. In fact, the only reason why is it parsed like this is because of
            performance reasons. It is easier to yield intents that are oneliners, rather than putting entire JSON file in memory (checking for
            brackets accross lines and then yielding valid JSON is pretty tough, so why not make both of our lives easier?)
        """

        in_dir = directory if directory else f"{self.intents_directory}/unparsed"
        out_dir = output_directory if output_directory != None else f"{in_dir}/../"

        return parse_all(directory=in_dir, output_directory=out_dir)


    def evaluate_intent_conditions(self, conditions: Union[Iterable[str], Iterator[str]], user: str=None) -> bool:
        solved = list()

        for condition in conditions:
            if "==" in condition:
                c = condition.strip().lower().split("==")

                if c[0] == "time":
                    if match(r"^(morning|early|beforenoon)$", c[1]):
                        x = is_time_between(time(3,00), time(8,00))
                        solved.append(x)
                
                    elif match(r"^(midday|noon|lunch(time)?)$", c[1]):
                        x = is_time_between(time(11,30), time(12,30))
                        solved.append(x)

                    elif match(r"^(afternoon|after( )?lunch)$", c[1]):
                        x = is_time_between(time(12,30), time(17,00))
                        solved.append(x)

                    elif match(r"^(evening)$", c[1]):
                        x = is_time_between(time(17,00), time(22,00))
                        solved.append(x)

                    elif match(r"^(night)$", c[1]):
                        x = is_time_between(time(22,00), time(1,00))
                        solved.append(x)

                    else:
                        if "-" in c[1]:
                            times = c[1].split("-")
                            parsed = [datetime.strptime(time, "%H:%M").time() for time in times]
                            x = is_time_between(parsed[0], parsed[1])

                            solved.append(x)

                        else:
                            required = datetime.strptime(c[1], "%H:%M").time()
                            now = time(datetime.now().hour, datetime.now().minute)

                            solved.append(now == required)

                elif c[0] == "user_data":
                    user_data = self.get_user_data(user)

                    if ":" in c[1]:
                        pair = c[1].split(":", maxsplit=1)

                        if str(user_data.get(pair[0], None)).lower() == pair[1]:
                            solved.append(True)
                        else:
                            solved.append(False)
 
                    else:
                        if user_data.get(c[1], None) == True:
                            solved.append(True)
                        else:
                            solved.append(False)

                elif c[0] == "session_data":
                    if ":" in c[1]:
                        pair = c[1].split(":", maxsplit=1)
                        data = self.session_cache.get(user, {}).get(pair[0])
                        
                        if data:
                            if data == pair[1]:
                                solved.append(True)
                            else:
                                solved.append(False)

                        else:
                            return None

                    else:
                        data = self.session_cache.get(user, {}).get(c[1])

                        if data:
                            if data == True:
                                solved.append(True)
                            else:
                                solved.append(False)

                        else:
                            return None

                else:
                    return None
            else:
                return None

        return all(c == True for c in solved)


    def evaluate_intent_actions(self, user: str, actions: List[str]):
        solved = list()
        
        for raw_action in actions:
            if "=" in raw_action:
                action = raw_action.strip().lower().split("=", maxsplit=1)

                if action[0] == "user_data":
                    if ":" in action[1]:
                        pair = action[1].split(":", maxsplit=1)
                        self.update_user_data(pair[1], pair[2], user=user)

                    else:
                        self.update_user_data(action[1], True, user=user)

                elif action[0] == "session_data":
                    if ":" in action[1]:
                        pair = action[1].split(":", maxsplit=1)
                        self.session_cache.update({
                            user: {
                                str(pair[0]): pair[1]
                            }
                        })

                    else:
                        self.session_cache.update({
                            user: {
                                str(action[1]): True
                            }
                        })
                else:
                    return None
            else:
                return None

        return all(c == True for c in solved)
