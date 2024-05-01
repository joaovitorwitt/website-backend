###############################################################################
# Imports
###############################################################################
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Projects
from .serializers import ProjectsSerializers

###############################################################################
# Create New Project Implementation
###############################################################################
@api_view(['POST'])
def add_project(request):
    """
    This functions creates a new project by sending a POST request to the API with the necessary parameters in a JSON format.

    Args:
        project_image_url (str): the url corresponding to the project image

        project_title (str): The title of the project

        project_description (str): The description of the project

    Returns:
        Response: indicating whether the project was created or something went wrong
    """
    try:
        project_data = request.data
        project_serializer = ProjectsSerializers(data=project_data)

        if project_serializer.is_valid():
            project_serializer.save()
            return Response({"message": "project created"}, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "invalid credentials", "error": project_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        return Response({"unable to create project": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Update Project Implementation
###############################################################################
@api_view(['PUT'])
def update_project(request, id):
    try:
        project_for_update = Projects.objects.get(project_id=id)
        
        project_for_update.project_title = request.data["project_title"]
        project_for_update.project_description = request.data["project_description"]
        project_for_update.project_image_url = request.data["project_image_url"]

        project_for_update.save()

        return Response({"message": "project updated successfully"}, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({"message": "project update failed", "something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Delete Project Implementation
###############################################################################
@api_view(['DELETE'])
def delete_project(request, id):
    try:
        project_for_deletion = Projects.objects.get(project_id=id)
        project_for_deletion.delete()

        return Response({"message": "project deleted successfully"}, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({"message": "failed to delete project", "something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Retrieve Projects Implementation
###############################################################################
@api_view(['GET'])
def list_projects(request):
    try:
        projects = Projects.objects.all()
        projects_serializers = ProjectsSerializers(projects, many=True)
        return Response({"projects": projects_serializers.data})
    except:
        return Response({"message": "something went wrong"})
    
###############################################################################
# Retrieve Single Project Implementation
###############################################################################
@api_view(['GET'])
def list_single_project(request, id):
    try:
        project_for_listing = Projects.objects.get(project_id=id)
        project_serializer = ProjectsSerializers(project_for_listing)
        return Response({"message": "project retrieved successfully", "project": project_serializer.data}, status=status.HTTP_200_OK)
    
    except Exception as error:
        return Response({"message": "something went wrong", "error": str(error)}, status=status.HTTP_400_BAD_REQUEST)