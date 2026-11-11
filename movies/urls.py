from django.urls import path
from movies.views import ListMovie, DetailMovie
from rest_framework.routers import SimpleRouter
from .views import MovieViewSet

app_name = 'movies'

router = SimpleRouter()
router.register('movies', MovieViewSet, basename = "movies")

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view()),
    path('', ListMovie.as_view()),
] + router.urls

#Se invece vuoi usare solo MovieViewSet, puoi lasciare urlpatterns = router.urls.