


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


def merge_sort(arr, order = 'asc'):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right, order)

def merge(left, right, order = 'asc'):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    if order == 'desc':
        return result[::-1]

    return result




def recursive_filtering(request_data, tracker = 0, new_request_data = []): # pylint: disable=dangerous-default-value
    date_elements = []

    for element in request_data:
        date_elements.append(element['created_at'])

    sorted_dates = merge_sort(date_elements, 'desc')

    while len(new_request_data) != len(request_data):

        for element in request_data:
            if len(request_data) == len(new_request_data):
                    return new_request_data # pylint: disable=bad-indentation

            if sorted_dates[tracker] == element['created_at']:
                new_request_data.append(element)
                tracker += 1

                recursive_filtering(request_data, tracker, new_request_data)
            else:
                continue

    return new_request_data



def mount_response_message(response_type: str, code: int) -> dict:
    """
    This method is design in order to mount request dictionaries
    by making use of the response_type and the status code.

    Args:
        response_type (str): The type of response from the request, boils down to 'OK' or 'failed'.
        code (int): The status code from the request.

    Returns:
        dict: The formatted response from the request.
    """
    out = {
        'response': response_type,
        'status_code': code
    }

    return out
