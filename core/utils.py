


def mount_response_dict(rows: list, columns: list) -> list[dict]:
    """
    Simple algorithm to map a `columns` list to each row sublist 
    inside `rows` list, converting them to a dictionary.

    Args:
        rows (list): A 2D list containing the rows from the database.
        columns (list): A list of columns.

    Returns:
        list[dict]: A list of dictionaries each containing the column and its value
        from the row.

    Usage:
        >>> rows = [[123, 456], [789, 051]]
        >>> columns ['abc', 'def']
        >>> mount_response_dict(rows, columns)
        [
            {
                'abc': 123,
                'def': 456
            },
            {
                'abc': 789,
                'def': 051
            }
        ]
    """
    ref_value = len(columns)

    validate_response_dict(rows, ref_value)

    result = {}
    data = []

    for row in rows:
        for index, col in enumerate(columns):
            result[col] = row[index]

        data.append(result)
        result = {}

    return data


def validate_response_dict(lst: list, reference_value: int) -> bool:
    """
    Helper method to validate a section of rows inside a 2D
    list against a `reference_value`.

    Args:
        lst (list): The list that will be validated.
        reference_value (int): The value to be used as reference.

    Raises:
        ValueError: If one of the lists does not contain the correct number of elements.

    Returns:
        bool: When all the validation passes.

    Example:
        >>> cols = ['abc', 'def', 'ghi']
        >>> rows = [[1,2,3], [4,5,6], [7,8,9,0]]
        >>> validate_response_dict(rows, len(cols))
        ValueError: invalid length
    """
    for l in lst:
        if len(l) != reference_value:
            raise ValueError('invalid length')

    return True
