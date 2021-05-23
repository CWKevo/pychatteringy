from typing import Dict, Union, List


class Intent(dict):
    @property
    def file(self) -> str:
        """
            The directory & file where the intent is located
            (without .json extension, is used for intent's `id`).
        """
        f = self.get("file", "unknown")
        return f.replace(".json", "")


    @property
    def ratio(self) -> int:
        """The matched intent's ratio."""
        return self.get("ratio", 0)


    @property
    def entities(self) -> dict:
        """Raw `dict` of the intent's entities."""
        return self.get("entities", {})


    @property
    def data(self) -> dict:
        """Raw `dict` of the intent's actual data."""
        return self.get("data", {})


    @property
    def id(self) -> str:
        """
            The intent's ID. Contains filename of the intent and the specified ID.
            Has to be unique, so you won't experience trouble.
        """
        return f'{self.file}-{self.data.get("id", 0)}'


    @property
    def goto_only(self) -> bool:
        """Whether or not the intent is accessible only by the 'goto' intent function."""
        return self.data.get("goto_only", False)


    @property
    def user(self) -> Union[Dict[str, str], List[str]]:
        """Raw data of intent's user possible messages."""
        return self.data.get("user", list())


    @property
    def bot(self) -> Union[Dict[str, str], List[str]]:
        """Raw data of bot's possible responses."""
        return self.data.get("bot", list())


    @property
    def priority(self) -> float:
        """The intent's priority."""
        return self.data.get("priority", 0.5)


    @property
    def actions(self) -> List[str]:
        """Raw data of actions to perform when intent is matched."""
        return self.data.get("actions", list())


    @property
    def conditions(self) -> Union['Conditions', None]:
        """
            `Conditions` of an intent.
            If at least one condition is false, then `Conditions`' `else_responses` are chosen instead.
        """
        raw = self.data.get("conditions", {})

        if raw:
            return Conditions(raw)
        else:
            return Conditions({})


class Conditions(dict):
    @property
    def if_raw(self) -> Union[List[str], List[None]]:
        """Raw "if" data. All conditions must be `True`, else `else_responses` elses,"""
        return self.get("if", list())


    @property
    def else_responses(self) -> Union[List[str], List[None]]:
        """A list of else responses. Returned if one or more conditions aren't met."""
        return self.get("else", list())
