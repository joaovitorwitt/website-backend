import unittest
from unittest import TestCase

from entities.project import Project

class ProjectTestCase(TestCase):

    def setUp(self) -> None:
        self.project_data = {
            'title': 'project title',
            'description': 'project description',
            'content': 'https://example.com',
            'image_url': 'https://example.com'

        }
        self.project = Project(**self.project_data)

    def test_initialization(self):
        self.assertEqual(self.project.title, 'Project Title')
        self.assertEqual(self.project.description, 'project description')
        self.assertEqual(self.project.content, 'https://example.com')
        self.assertEqual(self.project.image_url, 'https://example.com')

    def test_project_modification(self):
        self.assertEqual(self.project.description, 'project description')
        self.project['description'] = 'new description'
        self.assertEqual(self.project.description, 'new description')

    def test_project_representation(self):
        self.assertIsInstance(self.project, Project)

    def test_project_string(self):
        self.assertEqual(f"{self.project}", "Title: 'Project Title' || Description: 'project description'")

    def test_project_length(self):
        self.assertEqual(len(self.project), 8)

    def test_project_get_item(self):
        self.assertEqual(self.project['title'], 'Project Title')

    def test_project_set_item(self):
        self.assertEqual(self.project['content'], 'https://example.com')
        self.project['content'] = 'new url'
        self.assertEqual(self.project['content'], 'new url')


if __name__ == '__main__':
    unittest.main()
