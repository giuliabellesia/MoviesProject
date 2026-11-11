from django.shortcuts import render
from rest_framework import generics, viewsets #accesso a tutte CRUD senza doverle dividere in views
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DetailMovie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieViewSet(viewsets.ModelViewSet){
    queryset = Movie.object.all()
    serializer_class = MovieSerializer
}
