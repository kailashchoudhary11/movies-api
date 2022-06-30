from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from django.db.models import Q
import requests
from dotenv import load_dotenv
import os
# Create your views here.
load_dotenv()

class MovieAPI(APIView):
    def get(self, request, format=None):
        title = str(request.query_params.get(key="title"))
        try: 
            movie = Movie.objects.get(title=title)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Exception:
            apikey = os.getenv("api")
            url = f"https://www.omdbapi.com/?t={title}&apikey={apikey}"
            response = requests.get(url)
            if response.json().get('Response', None) != "False":
                tit = response.json()["Title"]
                year = response.json()["Year"]
                genre = response.json()["Genre"].split(": ")[0]
                genre = genre.split(", ")
                rating = response.json()["imdbRating"]
                id = response.json()["imdbID"]
                movie = Movie.objects.create(id=id, title=tit.lower(), released_year=year, genres=genre, rating=rating)
                serializer = MovieSerializer(movie)

                return Response(serializer.data)
        return Response({"error": "Movie with given title does not exist."})
        

class IdAPI(APIView):
    def get(self, request, format=None):
        id = str(request.query_params.get(key="id"))
        if id is not None:
            try:
                movie = Movie.objects.get(id=id)
                serializer = MovieSerializer(movie)
                return Response(serializer.data)
            except Exception:
                pass
        return Response({"error": "Movie with given id does not exist."})

class YearAPI(APIView):
    def get(self, request, format=None):
        year = str(request.query_params.get(key="year"))
        if year is not None:
            try:
                movies = Movie.objects.filter(released_year=year)
                if len(movies) == 0:
                    raise Exception
                serializer = MovieSerializer(movies, many=True)
                return Response(serializer.data)
            except Exception:
                pass
        return Response({"error": "No movies found in given year."})

class RatingAPI(APIView):
    def get(self, request, format=None):
        rating = str(request.query_params.get(key="rating"))
        if rating is not None and float(rating) < 10:
            try:
                movies = Movie.objects.filter(~Q(rating="N/A"), rating__gt=rating)
                if len(movies) == 0:
                    raise Exception
                serializer = MovieSerializer(movies, many=True)
                return Response(serializer.data)
            except Exception:
                pass
        return Response({"error": f"No movies found with rating higher than {rating}"})

class GenresAPI(APIView):
    def get(self, request, format=None):
        genre = str(request.query_params.get(key="genre"))
        if genre is not None:
            try:
                movies = Movie.objects.filter(genres__contains=genre.capitalize())
                if len(movies) == 0:
                    raise Exception
                serializer = MovieSerializer(movies, many=True)
                return Response(serializer.data)
            except Exception:
                pass
        return Response({"error": f"No movies found with given genre."})
