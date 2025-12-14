from datetime import datetime


def normalize_date(date: datetime) -> str:
    """
    This method is used when to extract a normalized format
    for object instances. 

    Returns:
        str: The datetime object converted to string in the following format: "month day, year"

    Example:
        >>> normalize_date()
        'August 12, 2024'
    """
    month = date.strftime('%B')
    day = date.day
    year = date.year
    return f'{month} {day}, {year}'

def format_title_for_url(title: str) -> str:
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

def format_title_for_displaying(title: str) -> str:
    """
    This method takes a setence and if possible converts
    each first letter of every word to uppercase.

    Args:
        title (str): the title to be formated.

    Returns:
        str: The formatted title with the first letter of each word capitalized.

    Example:
        >>> _format_title_for_displaying('how the measurament of units changed physics forever')
        'How The Measurament Of Units Changed Physics Forever'
    """
    title = title.lower()
    token = title.split()
    new_list = []

    for word in token:
        word = word.capitalize()
        new_list.append(word)

    return ' '.join(new_list)
