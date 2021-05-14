from typing import Union, List, Iterable, Iterator

from datetime import time
from helpers import is_time_between


def evaluate_intent_conditions(conditions: Union[Iterable[str], Iterator[str]]) -> bool:
    all = list()
    
    if type(conditions) == list:
        for condition in conditions:
            c = condition.strip().lower().split(":")

            if c[0] == "time":
                if c[1] == "morning":
                    x = is_time_between(time(3,00), time(8,00))
                    all.append(x)
            
                elif c[1] == "noon" or c[1] == "lunch":
                    x = is_time_between(time(11,30), time(12,30))
                    all.append(x)

                else:
                    all.append(False)
            else:
                return None
 
        return all(c == True for c in all)

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
        return evaluate_intent_conditions(self.if_raw)
