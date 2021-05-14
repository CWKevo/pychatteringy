from typing import Union, List, Iterable, Iterator

from re import match
from datetime import strptime, time
from helpers import is_time_between


def evaluate_intent_conditions(conditions: Union[Iterable[str], Iterator[str]]) -> bool:
    all = list()
    
    if type(conditions) == list:
        for condition in conditions:
            c = condition.strip().lower().split(";")

            if c[0] == "time":
                if match(r"^(morning|early|beforenoon)$", c[1]):
                    x = is_time_between(time(3,00), time(8,00))
                    all.append(x)
            
                elif match(r"^(midday|noon|lunch(time)?)$", c[1]):
                    x = is_time_between(time(11,30), time(12,30))
                    all.append(x)

                elif match(r"^(afternoon|after( )?lunch)$", c[1]):
                    x = is_time_between(time(12,30), time(17,00))
                    all.append(x)

                elif match(r"^(evening)$", c[1]):
                    x = is_time_between(time(17,00), time(22,00))
                    all.append(x)

                elif match(r"^(night)$", c[1]):
                    x = is_time_between(time(22,00), time(1,00))
                    all.append(x)

                else:
                    # TODO: Compactify:
                    times = c[1].split("-")
                    time1 = strptime(times[0], "%k:%M").time()
                    time2 = strptime(times[1], "%k:%M").time()
                    x = is_time_between(time1, time2)

                    all.append(x)
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
