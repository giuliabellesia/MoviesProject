from django.urls import path
from movies.views import ListMovie, DetailMovie
from rest_framework.routers import SimpleRouter
from .views import MovieViewSet, StreamingChannelViewSet

app_name = 'movies'

router = SimpleRouter()
router.register('movies', MovieViewSet, basename = "movies")
router.register('streaming-channel', StreamingChannelViewSet, basename= "streaming-channel")

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view()),
    path('', ListMovie.as_view()),
] + router.urls #ci restituisce pattern completo quando registriamo entrambi routers



#Se invece vuoi usare solo router registrati, puoi lasciare urlpatterns = router.urls.