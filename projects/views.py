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
    Create a new project entry in the database via a POST request.

    This function handles the creation of a new project by accepting JSON data in a POST request. It
    validates this data using a serializer. If the data is valid, the project is saved to the database
    and a success response is returned. If the data validation fails, an error response with details
    of the validation errors is returned. Any other exceptions during the creation process are caught
    and an appropriate error response is generated.

    Args:
        request (HttpRequest): The request object containing the project data in the `data` attribute.
            Expected JSON keys in this data include:
            - project_image_url (str): The URL for the project's image.
            - project_title (str): The title of the project.
            - project_description (str): A detailed description of the project.

    Returns:
        Response: A Response object with a JSON body that includes a success or error message.
            Possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the project is successfully created, with a message "Project created".
            - 400 (HTTP_400_BAD_REQUEST) if the provided data is invalid, detailing the validation errors,
              or if an unexpected error occurs, providing an error message.

    Raises:
        Exception: Catches general exceptions that might occur during the project creation process,
            particularly during data validation or database operations.
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
    """
    Update an existing project entry in the database via a PUT request.

    This function processes a PUT request to update a project identified by the provided ID with the new data
    supplied in the request. The function attempts to retrieve the specified project, updates its fields,
    and saves the changes. If the project is successfully updated, a success response is returned. If the
    project cannot be found or an error occurs during the update process, an error response is generated.

    Args:
        request (HttpRequest): The request object containing the new data for the project in the `data` attribute.
            Expected keys in this data include:
            - project_title (str): The updated title of the project.
            - project_description (str): The updated description of the project.
            - project_image_url (str): The updated URL for the project's image.
        id (int or str): The unique identifier of the project to be updated.

    Returns:
        Response: A Response object with a JSON body that includes a success or error message.
            Possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the project is successfully updated, with a message "Project updated successfully".
            - 400 (HTTP_400_BAD_REQUEST) if the project cannot be found or an unexpected error occurs,
              with a message detailing the error.

    Raises:
        Exception: Catches general exceptions that might occur during the project update process,
            particularly during database operations or data handling.
    """
    try:
        project_for_update = Projects.objects.get(project_id=id)
        
        if "project_title" in request.data:
            project_for_update.project_title = request.data["project_title"]

        if "project_description" in request.data:
            project_for_update.project_description = request.data["project_description"]

        if "project_image_url" in request.data:
            project_for_update.project_image_url = request.data["project_image_url"]

        if "project_link" in request.data:
            project_for_update.project_link = request.data["project_link"]

        project_for_update.save()

        return Response({"message": "project updated successfully"}, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({"message": "project update failed", "something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Delete Project Implementation
###############################################################################
@api_view(['DELETE'])
def delete_project(request, id):
    """
    Delete an existing project from the database via a DELETE request.

    This function processes a DELETE request to remove a project identified by the provided ID from the database.
    If the project is found and successfully deleted, a success response is returned. If the project cannot be
    found, or if an error occurs during the deletion process, an error response is generated with appropriate
    details.

    Args:
        request (HttpRequest): The request object, which is not used in this function but is required by the
            @api_view decorator to handle the HTTP method.
        id (int or str): The unique identifier of the project to be deleted.

    Returns:
        Response: A Response object with a JSON body that includes a success or error message. Possible HTTP
            status codes include:
            - 200 (HTTP_200_OK) if the project is successfully deleted, with a message "Project deleted successfully".
            - 400 (HTTP_400_BAD_REQUEST) for any other exceptions that occur during the deletion process,
              with a message detailing the error.

    Raises:
        Projects.DoesNotExist: Specifically catches and handles the case where no project with the provided
            ID is found in the database.
        Exception: Catches general exceptions that might occur during the project deletion process,
            particularly during database operations.
    """
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
    """
    Retrieve a list of all projects from the database.

    This function processes a GET request to fetch and serialize all projects stored in the database.
    The serialized data is then returned in a JSON format. If the operation is successful, the response 
    contains the list of projects. If an exception occurs during the retrieval or serialization process, 
    a generic error response is generated.

    Args:
        request (HttpRequest): The request object, which is not used in this function but is required by
            the @api_view decorator to handle the HTTP method.

    Returns:
        Response: A Response object with a JSON body that includes either the list of serialized project
            data or a generic error message. The HTTP status codes returned are:
            - 200 (HTTP_200_OK) if the projects are successfully retrieved, with the key "projects" containing
              the serialized data.
            - 500 (HTTP_500_INTERNAL_SERVER_ERROR) if an exception occurs during the retrieval or serialization
              process, with a message "Something went wrong".

    Raises:
        Exception: Catches general exceptions that might occur during the project listing process,
            particularly during database operations or data serialization.
    """
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
    """
    Retrieve a single project from the database based on its unique ID.

    This function processes a GET request to find and return a project identified by the provided ID.
    The project data, if found, is serialized into JSON format and included in the response. If the 
    operation is successful, the response contains the serialized project data. If the project cannot 
    be found, or if an error occurs during the retrieval process, an error response is generated detailing 
    the issue.

    Args:
        request (HttpRequest): The request object, which is not used in this function but is required by 
            the @api_view decorator to handle the HTTP method.
        id (int or str): The unique identifier of the project to be retrieved.

    Returns:
        Response: A Response object with a JSON body that includes either the serialized project data 
            or an error message. Possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the project is successfully retrieved, with a message "Project retrieved 
              successfully" and the project data.
            - 400 (HTTP_400_BAD_REQUEST) for any other exceptions that occur during the retrieval process, 
              with a message detailing the error.

    Raises:
        Projects.DoesNotExist: Specifically catches and handles the case where no project with the provided
            ID is found in the database.
        Exception: Catches general exceptions that might occur during the project retrieval process,
            particularly during database operations or data serialization.
    """
    try:
        project_for_listing = Projects.objects.get(project_id=id)
        project_serializer = ProjectsSerializers(project_for_listing)
        return Response({"message": "project retrieved successfully", "project": project_serializer.data}, status=status.HTTP_200_OK)
    
    except Exception as error:
        return Response({"message": "something went wrong", "error": str(error)}, status=status.HTTP_400_BAD_REQUEST)