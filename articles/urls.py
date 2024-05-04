###############################################################################
# Imports
###############################################################################
from . import views

from django.urls import path, include

###############################################################################
# Article Endpoints Implementation
###############################################################################
urlpatterns = [
    path("get/articles/", views.list_articles, name="list_articles"),
    path("create/article/", views.create_article, name="create-article"),
    path("delete/article/<int:id>", views.delete_article, name="delete-article"),
    path("update/article/<int:id>", views.update_article, name="update-article"),
    path("get/article/<int:id>", views.list_single_article, name="single-article")
]