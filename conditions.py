from typing import Union, List

from datetime import time
from helpers import is_time_between


def evaluate_intent_condition(condition: Union[List[str], None]) -> bool:
    if condition and type(condition) == list:
        c0 = condition[0].lower()
        c1 = condition[1].lower()

        if c0 == "time":
            if c1 == "morning":
                return is_time_between(time(3,00), time(8,00))
            
            elif c1 == "noon" or c1 == "lunch":
                return is_time_between(time(11,30), time(12,30))

            else:
                return False
        else:
            return None
    else:
        return None


class Condition(dict):
    @property
    def if_raw(self) -> Union[str, None]:
        return self.get("if", None)


    @property
    def else_responses(self) -> List[str]:
        return self.get("else", list())


    @property
    def state(self) -> bool:
        raw = self.if_raw
        try:
            split = raw.split(":", maxsplit=1)
        except AttributeError:
            split = None

        return evaluate_intent_condition(split)
