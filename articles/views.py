###############################################################################
# Imports
###############################################################################
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer
from .models import Articles

###############################################################################
# Article Creation Implementation
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
            return Response({"message": "Article created successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "invalid data provided", "message": article_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        return Response({"something went wrong": str(error)})

###############################################################################
# Article Deletion Implementation
###############################################################################
@api_view(['DELETE'])
def delete_article(request, id):
    """
    Endpoint to delete an article based on its unique ID.

    Args:
        id (int): The unique identifier of the article to be deleted.

    Returns:
        Response: A Response object indicating whether the article was successfully deleted.
            If the article is successfully deleted, a message indicating the deletion is returned.
            If an error occurs during the deletion process, an error message is returned.
    """
    try:
        article_for_deletion = Articles.objects.get(id=id)
        article_for_deletion.delete()
        return Response({"message": "article deleted"}, status=status.HTTP_200_OK)
    
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Article Update Implementation
###############################################################################
@api_view(['PUT'])
def update_article(request, id):
    """
    Sends a PUT request for the update of a specific article based on the ID

    Args:
        id (str):
            The actual ID of the article that we want to update

    Returns:
        Response: indicating whether the update of the article was succesful or not

    """
    try:
        article_for_update = Articles.objects.get(id=id)

        if "title" in request.data:
            article_for_update.title = request.data["title"]

        if "description" in request.data:
            article_for_update.description = request.data["description"]

        if "content" in request.data:
            article_for_update.content = request.data["content"]

        if "thumbnail" in request.data:
            article_for_update.thumbnail = request.data["thumbnail"]

        article_for_update.save()

        return Response({"message": "article updated successfully"}, status=status.HTTP_200_OK)
    
    except Articles.DoesNotExist:
        return Response({"message": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as error:
        return Response({"something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Article Retrieve Implementation
###############################################################################
@api_view(['GET'])
def list_single_article(request, id):
    """
    Sends a GET request to the API to retrieve a single article based on the ID provided in the endpoint.

    Args:
        id: The corresponding ID for the article we want to retrieve

    Returns:
        Response: The response indicating whether the retrieve operation was successful or not
    """
    try:
        article = Articles.objects.get(id=id)
        article_serializer = ArticleSerializer(article)

        return Response({"message": "article retrieved successfully", "article": article_serializer.data}, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({"error": "article could not be retrieved", "something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################################
# Article List Implementation
###############################################################################
@api_view(['GET'])
def list_articles(request):
    """
    Sends a GET request to the corresponding API endpoint that returns a list of articles in the database.

    Returns:
        Response: If the operation was successful, it returns the list of articles in a dictionary format.
        otherwise raises a Bad Request error
    """
    try:
        article_list = Articles.objects.all()
        article_list_serializer = ArticleSerializer(article_list, many=True)
        return Response({"articles": article_list_serializer.data}, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({"something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)
