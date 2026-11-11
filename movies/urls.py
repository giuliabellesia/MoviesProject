from django.urls import path
from movies.views import ListMovie, DetailMovie
from rest_framework.routers import SimpleRouter
from .views import MovieViewSet

app_name = 'movies'

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view()),
    path('', ListMovie.as_view()),
]

router = SimpleRouter
router.register('movies', MovieViewSet, basename = "movies")

urlpatterns = router.urls
