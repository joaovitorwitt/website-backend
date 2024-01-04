from rest_framework import serializers
from .models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"


# class ContentImageSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ContentImagesInsideArticles
#         fields = "__all__"