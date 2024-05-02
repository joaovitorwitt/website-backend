###############################################################################
# Imports
###############################################################################
from rest_framework import serializers
from .models import Articles

###############################################################################
# Article Serializer Implementation
###############################################################################
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"
