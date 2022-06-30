from django.urls import path
from .views import MovieAPI, IdAPI, YearAPI, RatingAPI, GenresAPI
app_name = 'api'

urlpatterns = [
    path('title/', MovieAPI.as_view(), name="main"),
    path('id/', IdAPI.as_view(), name="id"),
    path('year/', YearAPI.as_view(), name="year"),
    path('rating/', RatingAPI.as_view(), name="rating"),
    path('genres/', GenresAPI.as_view(), name="genres"),
]
