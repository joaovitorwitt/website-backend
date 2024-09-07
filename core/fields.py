

from typing import Any


class Input:

    def __repr__(self) -> str:
        return self.__class__.__name__


class StringInput(Input):
    def __init__(self, value: Any) -> None:
        self.validate(value)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'Invalid type {value}. Only string is allowed')
        


class BoolInput:
    pass

class IntInput:
    pass

class UrlInput:
    pass
