from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from .models import Articles


# create articles
@api_view(['POST'])
def create_article(request):
    try:
        article_data = request.data
        article_serializer = ArticleSerializer(data=article_data)

        if article_serializer.is_valid():
            article_serializer.save()
            return Response({"message": "article created successfully"})


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
