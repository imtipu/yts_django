from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_yts_movies),
    path('movies/popular/', views.popular_movies, name='popular_movies'),
    path('movies/latest/', views.all_movies, name='latest_movies'),
    path('movies/', views.all_movies, name='all_movies'),
    path('movies/most-downloaded/', views.all_movies, name='most_downloaded_movies'),
    path('movies/most-rated/', views.all_movies, name='most_rated_movies'),
    path('movies/<int:pk>/<slug:slug>/', views.movie_details, name='movie_details'),
]
