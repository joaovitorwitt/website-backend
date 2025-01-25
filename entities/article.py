

from entities.base import BaseEntity

class Article(BaseEntity):

    tags: str | None = None

    def validate(self):
        pass
