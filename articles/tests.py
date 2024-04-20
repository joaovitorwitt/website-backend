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

    # def test_article_creation_with_incorrect_data_returns_error(self):
    #     url = reverse('create-article')
    #     data = {
    #         'title' : '',
    #         'content' : '',
    #     }

    #     response = self.client.post(url, data, format='json')
    #     breakpoint()
    #     self.assertEqual(response.data['message'], 'something went wrong')


    def test_article_creation_without_thumbnail_returns_error(self):
        url = reverse('create-article')
        data = {
            'thumbnail': '',
            'title': 'my title',
            'description': 'my description',
            'content': 'my content'
        }

        response = self.client.post(url, data, format='json')
        breakpoint()
        self.assertEqual(response.data['error'], 'invalid data provided')

        

    
