from typing import Union, Generator, List

import pathlib
ROOT = pathlib.Path(__file__).parent.absolute()
INTENTS_ROOT = f"{ROOT}/intents"

import json
from conditions import Conditions


class Intent(dict):
    @property
    def user(self) -> List[str]:
        return self.get("user", list())


    @property
    def bot(self) -> List[str]:
        return self.get("bot", list())


    @property
    def conditions(self) -> Union[Conditions, None]:
        raw = self.get("conditions", {})

        if raw:
            return Conditions(raw)
        else:
            return Conditions({})


def get_intents(intent_json_path: str=INTENTS_ROOT + "/generic.json") -> dict:
    with open(intent_json_path, "r", encoding="UTF-8") as intent_file:
        intent_json = json.load(intent_file) # type: dict
        return intent_json


def intent_generator(intents=get_intents()) -> Generator[Intent, None, None]:
    for intent in intents:
        yield Intent(intent)
