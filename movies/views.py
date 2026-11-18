from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Movie, StreamingChannel
from .serializers import MovieSerializer, StreamingSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class DetailMovie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StreamingChannelViewSet(viewsets.ModelViewSet):
    queryset = StreamingChannel.objects.all()
    serializer_class = StreamingSerializer
    permission_classes = [IsAdminOrReadOnly]
    

#def perform_create(self, serializer): #no pk non ancora associato a utente
 #   serializer.save(owner=self.request.user)