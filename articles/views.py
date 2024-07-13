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
    1st sends a POST request
    data = {article data for creastion}
    requests.post(url, data)

    1st get the data that was passed to the url
    2nd serialize the data
    3rd check if the article data is valid
    4th if it is valid we save to the database and return a success message
    else return an error message 
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
        return Response({"something went wrong": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###############################################################################
# Article Deletion Implementation
###############################################################################
@api_view(['DELETE'])
def delete_article(request, id):
    """
    Handle a DELETE request to remove an article from the database based on its unique ID.

    This function attempts to delete an article identified by the provided ID. If the article is found
    and successfully deleted, a success response is returned. If the article cannot be found, or if an
    error occurs during the deletion process, an appropriate error response is generated.

    Args:
        request (HttpRequest): The request object, which is not used in this function but is required
            by the @api_view decorator to handle the HTTP method.
        id (int): The unique identifier of the article to be deleted.

    Returns:
        Response: A Response object with a JSON body that includes a message about the outcome. The
            possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the article is successfully deleted, with a message "Article deleted".
            - 400 (HTTP_400_BAD_REQUEST) if an unexpected error occurs during the deletion process,
              with an error message detailing the issue.

    Raises:
        Exception: General exception if an error occurs that prevents the article's deletion, such
            as a database error.
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
    Update an article with the given ID using data provided in the request.

    This function handles a PUT request to update fields of an existing article specified by its ID.
    The article is retrieved from the database and updated with any provided fields including title,
    description, content, and thumbnail. If the article is successfully updated, a success response
    is returned. If the article with the specified ID does not exist, a 404 response is sent. Other
    errors during the update process return a 400 response with an error message.

    Args:
        request (HttpRequest): The request object containing data to update the article. Expected
            keys in `request.data` are 'title', 'description', 'content', and 'thumbnail', which
            correspond to the article's attributes.
        id (str): The ID of the article to be updated.

    Returns:
        Response: A Response object containing a JSON message about the success or failure
            of the operation. Possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the update is successful.
            - 404 (HTTP_404_NOT_FOUND) if no article with the given ID is found.
            - 400 (HTTP_400_BAD_REQUEST) if an exception occurs during processing.

    Raises:
        Articles.DoesNotExist: If no article with the provided ID is found in the database.
        Exception: If any other exception occurs during the update process.
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
    Retrieve a single article from the database based on its unique ID.

    This function processes a GET request to find and return an article identified by the provided ID.
    If the article is found, its data, serialized into JSON format, is included in the response. If no
    article with the provided ID exists, a not found error is returned. Any other exceptions triggered
    during the process are also caught and returned as an error response.

    Args:
        request (HttpRequest): The request object, which is not used in this function but is required
            by the @api_view decorator to handle the HTTP method.
        id (int or str): The unique identifier of the article to be retrieved.

    Returns:
        Response: A Response object with a JSON body that includes either the serialized article data
            or an error message. The possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the article is successfully retrieved, with a message "Article retrieved successfully"
              and the article data.
            - 404 (HTTP_404_NOT_FOUND) if no article with the given ID is found.
            - 400 (HTTP_400_BAD_REQUEST) for any other exceptions that occur during the retrieval process,
              with an error message detailing the issue.

    Raises:
        Articles.DoesNotExist: If no article with the provided ID is found in the database.
        Exception: Catches general exceptions that might occur during the article retrieval process,
            particularly during database operations or data serialization.
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
    Retrieve a list of all articles from the database.

    This function processes a GET request to fetch and return all articles stored in the database.
    The articles are serialized into JSON format and returned in the response. If the operation is
    successful, a list of articles is included in the response. If an exception occurs during the
    retrieval process, an error response is generated detailing the issue.

    Args:
        request (HttpRequest): The request object, which is not used in this function but is required
            by the @api_view decorator to handle the HTTP method.

    Returns:
        Response: A Response object with a JSON body that includes either the list of serialized article
            data or an error message. The possible HTTP status codes include:
            - 200 (HTTP_200_OK) if the articles are successfully retrieved, with a key "articles" containing
              the list of serialized data.
            - 400 (HTTP_400_BAD_REQUEST) for any exceptions that occur during the retrieval process,
              with an error message detailing the issue.

    Raises:
        Exception: Catches general exceptions that might occur during the article listing process,
            particularly during database operations or data serialization.
    """
    try:
        article_list = Articles.objects.all()
        article_list_serializer = ArticleSerializer(article_list, many=True)
        return Response({"articles": article_list_serializer.data}, status=status.HTTP_200_OK)

    except Exception as error:
        return Response({"something went wrong": str(error)}, status=status.HTTP_400_BAD_REQUEST)
