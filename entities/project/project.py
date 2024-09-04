
from core.base import BaseEntity
from core.criptography import generate_unique_id
from core.string import String


class Project(BaseEntity):
    
    def __init__(self, title, description, project_link, image_url) -> None:

        self.id = generate_unique_id()
        self.title = title
        self.description = description
        self.project_link = project_link
        self.image_url = image_url
        self.title_for_url = String._format_title_for_url(title)
        super().__init__()


    def __repr__(self) -> str:
        return 'Project(%r, %r, %r, %r, %r, %r)' % (self.id, self.title, self.description, self.project_link, self.image_url, self.title_for_url) # pylint: disable=consider-using-f-string
    