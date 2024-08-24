
from core.base import BaseEntity


class Article(BaseEntity):

    def __init__(self, title, description, content, image_url) -> None: # pylint: disable=too-many-arguments

        self.title = title
        self.description = description
        self._creation_time = self.normalize_date()
        self.content = content
        self.image_url = image_url
        super().__init__()