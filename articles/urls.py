from django.urls import path, include
from . import views

urlpatterns = [
    path("get/articles/", views.list_articles, name="list_articles"),
    path("create/article/", views.create_article, name="create-article"),
    path("delete/article/<int:id>", views.delete_article, name="delete-article"),
    path("update/article/<int:id>", views.update_article, name="update-article"),
    path("get/article/<int:id>", views.list_single_article, name="single-article")
]

# GET articles - retrieves all the articles in the database

# GET article/{id} - retrieve a specific article by its id

# UPDATE article/edit/{id} - edit article based on its id

# DELETE article/delete/{id} - delete article based on its id 