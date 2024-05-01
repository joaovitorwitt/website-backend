###############################################################################
# Imports
###############################################################################
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from projects.models import Projects

###############################################################################
# Create New Project Test Case Implementation
###############################################################################
class CreateProjectTestCase(TestCase):

    def test_create_project_returns_expected_data_and_status(self):
        url = reverse('create-project')
        project_data = {
            'project_image_url': 'https://api.example.com/some-random-image',
            'project_title': 'title example',
            'project_description': 'some example description for the project'
        }
        response = self.client.post(url, project_data, format='json')

        self.assertEqual(response.data['message'], 'project created')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project_without_image_returns_error(self):
        url = reverse('create-project')
        project_data = {
            "project_image_url": "",
            "project_title": "some title",
            "project_description": "some description"
        }
        response = self.client.post(url, project_data, format='json')

        self.assertEqual(response.data['message'], 'invalid credentials')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_project_without_title_returns_error(self):
        url = reverse('create-project')
        project_data = {
            "project_image_url": "https://api.example.com/some-random-image",
            "project_title": "",
            "project_description": "some description"
        }
        response = self.client.post(url, project_data, format='json')

        self.assertEqual(response.data['message'], 'invalid credentials')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_project_without_description_returns_error(self):
        url = reverse('create-project')
        project_data = {
            "project_image_url": "https://api.example.com/some-random-image",
            "project_title": "some title",
            "project_description": ""
        }
        response = self.client.post(url, project_data, format='json')

        self.assertEqual(response.data['message'], 'invalid credentials')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

###############################################################################
# Update Project Test Case Implementation
###############################################################################
class UpdateProjectTestCase(TestCase):
    
    def setUp(self):
        self.project = Projects.objects.create(
            project_image_url='https://api.example.com/some-random-image',
            project_title='some title',
            project_description='some description'
        )

    def test_update_project_returns_expected_data_and_status(self):
        url = reverse('update-project', kwargs={'id': self.project.project_id})
        client = APIClient()
        data = {
        "project_title": "Updated Title",
        "project_description": "Updated Description",
        "project_image_url": "http://example.com/updated_image.jpg"
        }   
        response = client.put(url, data=data)

        self.assertEqual(response.data['message'], 'project updated successfully')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project_with_non_existent_project(self):
        project_data = {
            'project_id': 123,
            "project_title": "Updated Title",
            "project_description": "Updated Description",
            "project_image_url": "http://example.com/updated_image.jpg"
        }

        url = reverse('update-project', kwargs={'id': project_data['project_id']})
        client = APIClient()
        response = client.put(url)

        self.assertEqual(response.data['message'], 'project update failed')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

###############################################################################
# Delete Project Test Case Implementation
###############################################################################
class DeleteProjectTestCase(TestCase):
    
    def setUp(self):
        self.project = Projects.objects.create(
            project_image_url='https://api.example.com/some-random-image',
            project_title='some title',
            project_description='some description'
        )

    def test_delete_project_returns_expected_data_and_status(self):
        url = reverse('delete-project', kwargs={'id': self.project.project_id})
        client = APIClient()
        response = client.delete(url)

        self.assertEqual(response.data['message'], 'project deleted successfully')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_project_with_non_existent_project_returns_error(self):
        project_data = {
            'project_id': 123,
            "project_title": "Updated Title",
            "project_description": "Updated Description",
            "project_image_url": "http://example.com/updated_image.jpg"
        }
        url = reverse('delete-project', kwargs={'id': project_data['project_id']})
        client = APIClient()
        response = client.delete(url)

        self.assertEqual(response.data['message'], 'failed to delete project')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

###############################################################################
# Retrieve Project Test Case Implementation
###############################################################################
class RetrieveProjectTestCase(TestCase):
    
    def setUp(self):
        self.project = Projects.objects.create(
            project_image_url='https://api.example.com/some-random-image',
            project_title='some title',
            project_description='some description'
        )

    def test_retrieve_project_returns_expected_data_and_status(self):
        url = reverse('list-project', kwargs={'id': self.project.project_id})
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.data['message'], 'project retrieved successfully')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_project_with_non_existent_project_returns_error(self):
        project_data = {
            'project_id': 123,
            "project_title": "Updated Title",
            "project_description": "Updated Description",
            "project_image_url": "http://example.com/updated_image.jpg"
        }

        url = reverse("list-project", kwargs={'id': project_data['project_id']})
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.data['message'], 'something went wrong')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        