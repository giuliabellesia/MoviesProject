from django.shortcuts import render
from rest_framework import generics, viewsets, permissions #accesso a tutte CRUD senza doverle dividere in views
from .models import Movie
from .serializers import MovieSerializer
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class DetailMovie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,) #permissions.AllowAny, )

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)