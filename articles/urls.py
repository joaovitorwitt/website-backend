from django.urls import path, include
from . import views

urlpatterns = [
    path("articles/", views.test_endpoint, name="test")
]

# GET articles - retrieves all the articles in the database

# GET article/{id} - retrieve a specific article by its id

# UPDATE article/edit/{id} - edit article based on its id

# DELETE article/delete/{id} - delete article based on its id 