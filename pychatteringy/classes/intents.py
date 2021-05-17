from typing import Union, List


class Intent(dict):
    @property
    def id(self) -> int:
        return self.get("id", hash(str().join(self.user) + str().join(self.bot)))


    @property
    def user(self) -> List[str]:
        return self.get("user", list())


    @property
    def bot(self) -> List[str]:
        return self.get("bot", list())


    @property
    def priority(self) -> float:
        return float(self.get("priority", 0.5))


    @property
    def actions(self) -> List[str]:
        return self.get("actions", list())


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
