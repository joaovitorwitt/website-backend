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
        breakpoint()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Article created successfully")

    
