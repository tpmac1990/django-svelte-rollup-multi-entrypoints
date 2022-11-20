from taggit.serializers import TagListSerializerField, TaggitSerializer
from  rest_framework import serializers
from .models import Film


# TaggitSerializer required to use taggit with djangorestframework
class FilmSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Film
        fields = ['id', 'name', 'director', 'tags']