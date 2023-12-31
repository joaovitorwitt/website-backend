from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Projects
from .serializers import ProjectsSerializers


# Create your views here.

# @api_view(['POST'])
# def add_project(request):





@api_view(['GET'])
def list_projects(request):
    try:
        projects = Projects.objects.all()
        projects_serializers = ProjectsSerializers(projects, many=True)
        return Response({"projects": projects_serializers.data})
    except:
        return Response({"message": "something went wrong"})