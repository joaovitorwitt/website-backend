
from core.base import BaseEntity


class Article(BaseEntity):

    def __init__(self, title: str, description: str, content: str, image_url: str) -> None: # pylint: disable=too-many-arguments

        self.title = title
        self.description = description
        self._creation_time = None
        self.content = content
        self.image_url = image_url
        self.url_title = self._format_title_for_url(self.title)
        super().__init__()