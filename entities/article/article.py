
from typing import Any
from core.base import BaseEntity
from core.string import String
from core.criptography import generate_unique_id

class Article(BaseEntity):

    def __init__(self, title: str, description: str, content: str, image_url: str) -> None: # pylint: disable=too-many-arguments

        self.id = generate_unique_id()
        self.title = title
        self.description = description
        self._creation_time = 123
        self.content = content
        self.image_url = image_url
        self.url_title = String._format_title_for_url(self.title)
        super().__init__()

    def __repr__(self) -> str:
        """
        This dunder method is used to display a string representation for the class,
        this method is usually intended for the programmer, for this reason I am 
        displaying all the information about the instance when we use `repr()`

        Returns:
            str: The string representation of the class
        """
        return 'Article(%r, %r, %r, %r, %r, %r)' % (self.title, self.description, self._creation_time, self.content, self.image_url, self.url_title) # pylint: disable=consider-using-f-string, line-too-long

    def __str__(self) -> str:
        """
        Similar to the `__repr__` method, this method also returns a string 
        representation of the class. This representation is usually intended for
        the user.

        Returns:
            str: A more informal representaion of the class
        """
        return 'Title: %r || Description: %r' % (self.title, self.description) # pylint: disable=consider-using-f-string

    def __len__(self) -> int:
        """
        This dunder method is called when we use `len()`.
        Here we will be modifying this to return the number of attributes
        in the instance.

        Returns:
            int: The number of attributes in the instance
        """
        return len(self.__dict__)

    def __getitem__(self, position: int) -> Any:
        """
        This dunder method is used to make the
        instance subscriptable when using the following
        syntax: `self[0]`.

        Args:
            position (int): The index to extract the element

        Returns:
            Any: The element in the instance at the given index.
        """
        # dont know if this is the best approach to extract an element at a given index
        return list(self.__dict__.values())[position]
    

