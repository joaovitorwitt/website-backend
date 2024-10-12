import uuid

def generate_unique_id():
    """
    This method is used to generate a hexadecimal
    string of 16 characters to serve as an unique ID
    for the entities.

    Example:
        >>> generate_unique_id()
        '6e54792f2ee44b5ea5ffdba7a29312e3'
    """
    uid = uuid.uuid4()
    return uid.hex
