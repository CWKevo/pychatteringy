from typing import Union, Generator, List

import pathlib
ROOT = pathlib.Path(__file__).parent.absolute()
INTENTS_ROOT = f"{ROOT}/intents"

import json
from conditions import Condition


class Intent(dict):
    @property
    def user(self) -> List[str]:
        return self.get("user", list())


    @property
    def bot(self) -> List[str]:
        return self.get("bot", list())


    @property
    def condition(self) -> Union[Condition, None]:
        raw = self.get("condition", {})

        if raw:
            return Condition(raw)
        else:
            return Condition({})


def get_intent(intent_json_path: str=INTENTS_ROOT + "/generic.json") -> dict:
    with open(intent_json_path, "r", encoding="UTF-8") as intent_file:
        intent_json = json.load(intent_file) # type: dict
        return intent_json


def intent_generator(intent_dict: dict=get_intent()) -> Generator[Intent, None, None]:
    for intent in intent_dict:
        yield Intent(intent)
