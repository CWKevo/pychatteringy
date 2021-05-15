from typing import Union, List, Iterable, Iterator

from re import match
from datetime import datetime, time

from pychatteringy.functions.helpers import is_time_between


def evaluate_intent_conditions(conditions: Union[Iterable[str], Iterator[str]]) -> bool:
    solved = list()
    
    if type(conditions) == list:
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
                else:
                    return None
            else:
                return None
 
        return all(c == True for c in solved)

    else:
        return None
