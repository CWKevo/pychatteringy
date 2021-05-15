from typing import Union, List

from pychatteringy.functions.evaluation import evaluate_intent_conditions


class Intent(dict):
    @property
    def user(self) -> List[str]:
        return self.get("user", list())


    @property
    def bot(self) -> List[str]:
        return self.get("bot", list())


    @property
    def priority(self) -> float:
        return float(self.get("priority", 1.0))


    @property
    def conditions(self) -> Union['Conditions', None]:
        raw = self.get("conditions", {})

        if raw:
            return Conditions(raw)
        else:
            return Conditions({})


class Conditions(dict):
    @property
    def if_raw(self) -> Union[List[str], List[None]]:
        return self.get("if", list())


    @property
    def else_responses(self) -> Union[List[str], List[None]]:
        return self.get("else", list())


    @property
    def state(self) -> bool:
        return evaluate_intent_conditions(self.if_raw)
