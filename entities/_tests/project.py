import unittest
from unittest import TestCase


from entities.project import Project

class ProjectTestCase(TestCase):

    def setUp(self) -> None:
        self.project = Project(
            title='Project Title',
            description='project description',
            project_link='https://example.com',
            image_url='https://example.com'
        )

    def test_project_creation(self):
        pass


if __name__ == '__main__':
    unittest.main()
