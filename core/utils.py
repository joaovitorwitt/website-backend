


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
    result = {}
    data = []

    for row in rows:
        for index, col in enumerate(columns):
            result[col] = row[index]

        data.append(result)
        result = {}

    return data
