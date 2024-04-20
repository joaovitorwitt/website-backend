###############################################################################
# Imports
###############################################################################
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer
from .models import Articles


###############################################################################
# Implementation
###############################################################################
@api_view(['POST'])
def create_article(request):
    """
    Creates an article instance.
    This endpoint allows the creation of a new article by accepting a POST request with the necessary data in the request body.

    Args:
        thumbnail (str):
            The string representing the image url for the article

        title (str):
            The title of the article
        
        description (str):
            The description of the article

        publish_date (Date):
            The current datetime that the article is being published

        content (str):
            The actual content of the article

    Returns:
        Response: returns the response indicating whether or not the article creation was successfull 
    """
    try:
        article_data = request.data

        article_serializer = ArticleSerializer(data=article_data)

        if article_serializer.is_valid():
            article_serializer.save()
            return Response({"message": "Article created successfully"})
        
        else:
            return Response({"something went wrong": article_serializer.errors})

    except Exception as error:
        return Response({"something went wrong": str(error)})


# delete articles
@api_view(['DELETE'])
def delete_article(request, id):
    try:
        article_for_deletion = Articles.objects.get(id=id)
        article_for_deletion.delete()
        return Response({"message": "article deleted"})
    
    except Exception as error:
        return Response({"error": str(error)})

# update articles
@api_view(['PUT'])
def update_article(request, id):
    try:
        article_for_update = Articles.objects.get(id=id)

        # Update title if present in request data
        if "title" in request.data:
            article_for_update.title = request.data["title"]

        # Update description if present in request data
        if "description" in request.data:
            article_for_update.description = request.data["description"]

        # Update content if present in request data
        if "content" in request.data:
            article_for_update.content = request.data["content"]

        # Update thumbnail if present in request data
        if "thumbnail" in request.data:
            article_for_update.thumbnail = request.data["thumbnail"]

        article_for_update.save()

        return Response({"message": "article updated successfully"})
    
    except Articles.DoesNotExist:
        return Response({"message": "Article not found"}, status=404)
    
    except Exception as error:
        return Response({"something went wrong": str(error)})


# list single article
@api_view(['GET'])
def list_single_article(request, id):
    try:
        article = Articles.objects.get(id=id)
        article_serializer = ArticleSerializer(article)

        return Response({"article": article_serializer.data})

    except Exception as error:
        return Response({"something went wrong": str(error)})


# list all articles
@api_view(['GET'])
def list_articles(request):
    try:
        article_list = Articles.objects.all()
        article_list_serializer = ArticleSerializer(article_list, many=True)
        return Response({"articles": article_list_serializer.data})

    except Exception as error:
        return Response({"something went wrong": str(error)})
