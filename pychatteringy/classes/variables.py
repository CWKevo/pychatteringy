import datetime


class GenericVariables():
    """
        Class representing generic variables that can be used in intents.

        ### Properties:
        - `time` - The current time, eg: 17:02.
        - `time12` - The current time in 12-hour format, eg. 05:02.
        - `date` - The current date.
    """

    @property
    def time(self) -> str:
        return datetime.datetime.now().strftime(r"%H:%M")


    @property
    def time12(self) -> str:
        return datetime.datetime.now().strftime(r"%I:%M")


    @property
    def date(self) -> str:
        return datetime.datetime.now().strftime(r"%d. %B %Y")


    @property
    def as_dict(self) -> dict:
        return {
            "time": self.time,
            "time12": self.time12,
            "date": self.date
        }
