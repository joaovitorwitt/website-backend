


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


def merge_sort(lst: list, order_type: str = 'asc'):
    if len(lst) > 1:

        # divide the list into two
        r = len(lst) // 2
        L = lst[:r]
        M = lst[r:]

        # sort the the two halves
        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        # until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = M[j]
                j += 1
            k += 1

        # when we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            lst[k] = M[j]
            j += 1
            j += 1

    # return the list reversed since we want to order by dates
    if order_type == 'desc':
        return lst[::-1]

    return lst


def sort_by_date(request_data: list) -> list:
    """
    This method is designed to work alongside
    GET requests to sort the elements by date
    using a merge sort algorithm.

    Args:
        request_data (list): The request date containing the elements for sorting.

    Returns:
        list: The final orded by date date
    """
    date_elements = []
    new_request_data = []

    tracker = 0

    for element in request_data:
        date_elements.append(element['created_at'])

    sorted_dates =  merge_sort(date_elements, 'desc')


    # breakpoint()
    for element in request_data:
        if sorted_dates[tracker] == element['created_at']:
            new_request_data.append(element)
            tracker += 1
            continue

            

    return new_request_data


def recursive_approach(request_data, tracker = 0, new_request_data = []):
    date_elements = []

    for element in request_data:
        date_elements.append(element['created_at'])

    sorted_dates = merge_sort(date_elements, 'desc')

    while len(new_request_data) != len(request_data):

        for element in request_data:
            if len(request_data) == len(new_request_data):
                    return new_request_data
            
            if sorted_dates[tracker] == element['created_at']:
                new_request_data.append(element)
                tracker += 1
                
                recursive_approach(request_data, tracker, new_request_data)
            else:
                continue

    return new_request_data
    
