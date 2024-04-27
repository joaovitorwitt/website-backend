###############################################################################
# Imports
###############################################################################
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

###############################################################################
# Article Creation TestCase Implementation
###############################################################################
class ArticleCreationTestCase(APITestCase):
    def test_article_creation_with_correct_data(self):
        url = reverse('create-article')
        data = {
            'title': 'Test Title',
            'content': 'The content',
            'thumbnail': 'https://api.example.com/some-random-thumbnail'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Article created successfully")

    def test_article_creation_without_thumbnail_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': '',
            'title': 'my title',
            'description': 'my description',
            'content': 'my content'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_without_title_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'https://api.example.com/some-random-thumbnail',
            'title': '',
            'description': 'my description',
            'content': 'my content'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_without_description_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'https://api.example.com/some-random-thumbnail',
            'title': 'my title',
            'description': '',
            'content': 'my content'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_without_content_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'https://api.example.com/some-random-thumbnail',
            'title': 'my title',
            'description': 'my description',
            'content': ''
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

    def test_article_creation_max_thumbnail_size(self):
        url = reverse('create-article')
        data = {
            'thumbnail': 'THIS STRING IS 256 CHARACTERS SASAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdsa',
            'title': 'my title',
            'description': 'my description',
            'content': 'my content'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'invalid data provided')

###############################################################################
# Article Deletion TestCase Implementation
###############################################################################
class ArticleDeletionTestCase(APITestCase):
    pass

###############################################################################
# Article Retrieve TestCase Implementation
###############################################################################
class ArticleRetrieveTestCase(APITestCase):
    pass

###############################################################################
# Article Update TestCase Implementation
###############################################################################