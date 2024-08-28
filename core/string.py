from datetime import datetime

import settings


class String:

    @classmethod
    def _normalize_date(cls) -> str:
        """
        This method is used when to extract a normalized format
        for object instances. 

        Returns:
            str: The datetime object converted to string in the following format: "month day, year"

        Example:
            >>> normalize_date()
            'August 12, 2024'
        """
        current_date = datetime.now()
        month = current_date.strftime('%B')
        day = current_date.day
        year = current_date.year
        return f'{month} {day}, {year}'

    @classmethod
    def _format_title_for_url(cls, title: str) -> str:
        """
        This private method takes a title and converts into
        a URL format by replacing whitespaces for hifens.

        Args:
            title (str): The title to be converted.

        Returns:
            str: The formatted title

        Example:
            >>> _format_title_for_url("How the Measurament of Units Changed Physics")
            'how-the-measurament-of-units-changed-physics'
        """
        new_title = title.lower().strip().replace(' ', '-')
        return new_title

    @classmethod
    def singularize(cls, string: str) -> str:
        """
        This method takes a plural form of a string
        and converts into its singular form

        Args:
            string (str): The string to be converted to singular

        Returns:
            str: The singularized string

        Example:
            >>> singularize('studies')
            'study'

            >>> singularize('watches')
            'watch'

            >>> singularize('computers')
            'computer'
        """
        string = string.lower()

        
        if string in settings.IMMUTABLE_PLURALS:
            return string

        if string in settings.IRREGULAR_NOUNS_PLURAL:
            string = cls._convert_irregular_plural_words(string)

        if string[-3:] == 'ies':
            string = string[:-3] + 'y'

        if string[-2:] == 'es':
            string = string[:-2]

        if string[-2:] == 'ys':
            string = string[:-2] + 'y'

        if string[-3:] == 'oes':
            string = string[:-2]

        if string[-2:] == 'os':
            string = string[:-1]

        return string


    @classmethod
    def pluralize(cls, string: str) -> str:

        if string[-1] == 'y' and string[-2] in settings.VOWELS:
            string += 's'

        if string [-1] == 'y' and string[-2] not in settings.VOWELS:
            string = string[:-1] + 'ies'

    @classmethod
    def _convert_irregular_plural_words(cls, word: str) -> str:
        """
        This private method will be called when one of the irregular
        nouns appear in the singularize method.

        Args:
            word (str): The irregular noun to be converted to singular.

        Returns:
            str: The corresponding singular version.
        """
        # word = 'teeth' it needs to return tooth
        some_dict = {
            'teeth': 'tooth',
            'children': 'child',
            'men': 'man',
            'women': 'woman',
            'person': 'people',
            'mouse': 'mice',
            'goose': 'geese'
        }

        # loop through this dictionary
        # get the key correspoding

        for key, value in some_dict.items():
            if word == key:
                return value
            
        raise ValueError('Something went wrong')




        

        

