
from entities.base import BaseEntity
from core.criptography import generate_unique_id
from core.string import format_title_for_displaying, format_title_for_url, normalize_date
from core.date import DateTime

class Project(BaseEntity):

    def __init__(self, title: str, description: str, content: str, image_url: str) -> None:
        self.id = generate_unique_id()
        self.title = format_title_for_displaying(title)
        self.description: str = description
        self.creation_time = DateTime.stringfy_date(DateTime.now())
        self.date = normalize_date(DateTime.now())
        self.content: str = content
        self.image_url: str = image_url
        self.url_title: str = format_title_for_url(self.title)
        super().__init__()


    def __repr__(self) -> str:
        return 'Project(%r, %r, %r, %r, %r, %r)' % (self.id, self.title, self.description, self.content, self.image_url, self.url_title) # pylint: disable=consider-using-f-string
    