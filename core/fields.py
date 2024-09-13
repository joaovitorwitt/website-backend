

from typing import Any


class BaseInput:

    def __repr__(self) -> str:
        """
        The __repr__ magic method is used in order
        to return the current class name.

        Returns:
            str: The name of the class
        """
        return self.__class__.__name__

class StringInput(BaseInput):
    """
    class designed to handle string values.
    """
    def __init__(self, value: Any) -> None:
        self.validate(value)

    def __repr__(self) -> str:
        return self.value

    def validate(self, value: str) -> None:
        """
        Validates whether the input value is a string
        or not, in the case of not being a string a 
        `TypeError` exception is raised.

        Args:
            value (str): The element that will be validated as a string.

        Raises:
            TypeError: If the `value` is not a string.

        Example:
            >>> str_input = StringInput('123')

            >>> not_str_input = StringInput(123)
            TypeError: Input 123 of type int is not a string.
        """
        if not isinstance(value, str):
            raise TypeError(f'Input {value} of type {type(value)} is not a string.')
        self.value = value


class BooleanInput(BaseInput):
    """
    Class designed to handle boolean values.
    """
    def __init__(self, value: Any) -> None:
        self.validate(value)

    def validate(self, value: Any) -> None:
        """
        Validates whether the given `value` is
        a boolean value or not.

        Args:
            value (Any): the value to be validated as a boolean.

        Raises:
            TypeError: If the value is not a boolean type.
        """
        if not isinstance(value, bool):
            raise TypeError(f'Input {value} of type {type(value)} is not a boolean.')
        self.value = value

class IntegerInput(BaseInput):
    """
    Class designed to handle integer values
    """
    def __init__(self, value: Any) -> None:
        self.validate(value)

    def validate(self, value: Any) -> None:
        """
        Validates whether a given `value` is 
        an integer or not.

        Args:
            value (Any): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f'Input {value} of type {type(value)} is not an integer.')
        self.value = value


class URLInput(BaseInput):
    pass
