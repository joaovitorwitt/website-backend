from typing import Any

# from core.postgres import PostgresConnection

class BaseEntity:

    # TODO implement magic methods here
    # these methods below will send a request based on the operation
    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


    def retrieve_single(self, id: Any):
        pass

    def retrieve_all(self):
        # retrieve all instances on the database for that entity
        # for that we need the instance name
        return self.__class__.__name__
        
