###############################################################################
# Imports
###############################################################################
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

###############################################################################
# Main View Implementation
###############################################################################
@api_view(['GET'])
def ping(request):
    return Response({"status": "success"})
