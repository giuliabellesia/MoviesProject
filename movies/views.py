from django.shortcuts import render
from rest_framework import generics, viewsets, permissions #accesso a tutte CRUD senza doverle dividere in views
from .models import Movie, StreamingChannel
from .serializers import MovieSerializer, StreamingSerializer
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

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
    permission_classes = (IsOwnerOrReadOnly,) #permissions.AllowAny, ) questo controllo xke non ci fidiamo

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StreamingChannelViewSet(viewsets.ReadOnlyModelViewSet): #definiamo solo queste tre cose
    queryset = StreamingChannel.objects.all()
    serializer_class = StreamingSerializer
    permission_classes = [IsAdminOrReadOnly] #permissions.AllowAny, ) 
    

#def perform_create(self, serializer): #no pk non ancora associato a utente
 #   serializer.save(owner=self.request.user)