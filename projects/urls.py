from django.urls import path, include
from . import views

urlpatterns = [
    path("get/projects/", views.list_projects, name="list-projects")
]