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


    def natural_day():
        # takes a date as argument 
        # checks if the date is today
        # checks if the date is yesterday
        # checks if the date is tomorrow

        pass

    def to_ordinal():
        pass




        

        

