from django.urls import path, include
from . import views

urlpatterns = [
    path("get/projects/", views.list_projects, name="list-projects"),
    path("create/project/", views.add_project, name="create-project"),
    path("update/project/<int:id>", views.update_project, name="update-project"),
    path("delete/project/<int:id>", views.delete_project, name="delete-project"),
    path("get/project/<int:id>", views.list_single_project, name="list-project")
]