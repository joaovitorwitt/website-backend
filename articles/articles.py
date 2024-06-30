###############################################################################
# Imports
###############################################################################
import requests
import os

import dotenv
from dotenv import load_dotenv


load_dotenv()
###############################################################################
# Article Implementation
###############################################################################
class Articles:

    def create(self):
        return os.getenv("API_URL")


    def delete(self):
        pass

    def update(self):
        pass

    def list_single(self):
        pass

    def list_many(self):
        pass


