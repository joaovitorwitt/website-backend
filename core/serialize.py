
import json
import pickle

from typing import Any


def dumps(obj: Any, protocol: str = 'json') -> Any:
    """
    Method to serialize python objects using a
    given `protocol`.

    Args:
        obj (Any): The object to be serialized.
        protocol (str): The type of protocol to use in the serialization. Defaults to 'json'.

    Raises:
        ValueError: If the protocol is not valid.

    Returns:
        Any: The serialized objected.

    Example:
        >>> data = {'key': 'value'}
        >>> dumps(data)
        '{"key": "value"}'
    """
    if protocol == 'json':
        return json.dumps(obj)

    if protocol == 'pickle':
        return pickle.dumps(obj)

    raise ValueError(f'Invalid protocol type: "{protocol}", options are "json" or "pickle".')

def loads(obj: Any, protocol: str = 'json'):
    """
    Method to deserialize a python object using
    a given `protocol`.

    Args:
        obj (Any): The object to be deserialized.
        protocol (str, optional): The type of protocol to used in the deserialization. Defaults to 'json'.

    Raises:
        ValueError: If the `protocol` is an invalid one.

    Returns:
        Any: The deserialized object.

    Example:
        >>> serialized_obj = '{"key": "value"}'
        >>> loads(serialized_obj)
    """
    if protocol == 'json':
        return json.loads(obj)

    if protocol == 'pickle':
        return pickle.loads(obj)

    raise ValueError(f'Invalid protocol type: "{protocol}", options are "json" or "pickle".')
    