from typing import Dict, Union, List


class Intent(dict):
    @property
    def file(self) -> str:
        return self.get("file", "unknown")

    @property
    def data(self) -> dict:
        return self.get("data", {})

    @property
    def id(self) -> str:
        return f'{self.file}-{self.data.get("id", 0)}'


    @property
    def user(self) -> Union[Dict[str, str], List[str]]:
        return self.data.get("user", list())


    @property
    def bot(self) -> Union[Dict[str, str], List[str]]:
        return self.data.get("bot", list())


    @property
    def priority(self) -> float:
        return self.data.get("priority", 0.5)


    @property
    def actions(self) -> List[str]:
        return self.data.get("actions", list())


    @property
    def conditions(self) -> Union['Conditions', None]:
        raw = self.data.get("conditions", {})

        if raw:
            return Conditions(raw)
        else:
            return Conditions({})


class Action(list):
    @property
    def action(self) -> str:
        return self[0]


    @property
    def values(self) -> list:
        return self[1].split(":")


class Conditions(dict):
    @property
    def if_raw(self) -> Union[List[str], List[None]]:
        return self.get("if", list())


    @property
    def else_responses(self) -> Union[List[str], List[None]]:
        return self.get("else", list())
