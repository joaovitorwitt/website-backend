from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Projects
from .serializers import ProjectsSerializers

import base64


@api_view(['POST'])
def add_project(request):
    try:
        project_data = request.data
        project_serializer = ProjectsSerializers(data=project_data)

        if project_serializer.is_valid():
            project_serializer.save()
            return Response({"message": "project created"})
        
        else:
            return Response({"error": project_serializer.errors})

    except Exception as error:
        return Response({"unable to create project": str(error)})


@api_view(['PUT'])
def update_project(request, id):
    try:
        # 1st - get the image that is currently in the database
        # go into the directory and delete the image
        
        project_for_update = Projects.objects.get(project_id=id)
        
        project_for_update.project_title = request.data["project_title"]
        project_for_update.project_description = request.data["project_description"]
        project_for_update.project_image_url = request.data["project_image_url"]

        project_for_update.save()

        return Response({"message": "project updated successfully"})

        pass

    except Exception as error:
        return Response({"something went wrong": str(error)})


@api_view(['DELETE'])
def delete_project(request, id):
    try:
        project_for_deletion = Projects.objects.get(project_id=id)
        project_for_deletion.delete()

        return Response({"message": "project deleted successfully"})

    except Exception as error:
        return Response({"something went wrong": str(error)})


@api_view(['GET'])
def list_projects(request):
    try:
        projects = Projects.objects.all()
        projects_serializers = ProjectsSerializers(projects, many=True)
        return Response({"projects": projects_serializers.data})
    except:
        return Response({"message": "something went wrong"})
    


@api_view(['GET'])
def list_single_project(request, id):
    try:
        project_for_listing = Projects.objects.get(project_id=id)
        project_serializer = ProjectsSerializers(project_for_listing)
        return Response({"project": project_serializer.data})
    
    except Exception as error:
        return Response({"error": str(error)})