from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DetailMovie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
