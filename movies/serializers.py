from  rest_framework import serializers
from .models import Movie, StreamingChannel

__all__ = ["MovieSerializer", 
           "StreamingSerializer"]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'subtitle', 'director', 'description']

class StreamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingChannel
        fields = ['id', 'name', 'film']