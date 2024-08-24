
from datetime import datetime


class String:
    
    @classmethod
    def normalize_date(cls) -> str:
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
        month = current_date.strftime('%B') # returns month name in full format - if we pass %b we get the abbreviated version
        day = current_date.day
        year = current_date.year
        return f'{month} {day}, {year}'


    @classmethod
    def format_title_for_url(cls, title: str) -> str:
        # receives a title like this:
        # How the Measurament of Units Changed Physics

        # and converts to something like this:
        # how-the-measurement-of-units-changed-physics

        new_title = title.lower().strip().replace(' ', '-')
        return new_title



