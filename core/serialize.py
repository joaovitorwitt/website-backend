
import json
import pickle

from typing import Any

class SerializeObject():

    def dumps(self, obj: Any, protocol: str):

        if protocol == 'json':
            return json.dumps(obj)

        if protocol == 'pickle':
            return pickle.dumps(obj)

        raise ValueError('Invalid protocol type, options are "json" or "pickle"')

    def loads(self, obj: Any, protocol: str):

        if protocol == 'json':
            return json.loads(obj)

        if protocol == 'pickle':
            return pickle.loads(obj)

        raise ValueError(f'Invalid protocol type: {protocol}, options are "json" or "pickle"')

    