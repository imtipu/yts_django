from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.
from .models import *


def home(request):
    data = {
        'title': 'Movies',
    }
    return render(request, 'home.html', data)


@csrf_exempt
def add_yts_movies(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            try:
                YTSMovie.objects.create(
                    yts_id=data.get('id'),
                )
                return HttpResponse(data.get('id') + '. ' + data.get('title') + ' -- Added')
            except:
                return HttpResponse('No Data')

        return HttpResponse('No Data')


def all_movies(request):
    page = ''
    url = "https://yts.mx/api/v2/list_movies.json"
    if request.GET.get('page'):
        url = "https://yts.mx/api/v2/list_movies.json?page="+request.GET.get('page')

    res = requests.get(url)
    res.encoding = "utf-8"
    result = res.json()
    movies = result["data"]["movies"]
    data = {
        'movies': movies,
    }

    return render(request, 'all_movies.html', data)


def movie_details(request, pk, slug):
    url = 'https://yts.mx/api/v2/movie_details.json?movie_id=' \
          + str(pk) + \
          '&with_images=true&with_cast=true'
    res = requests.get(url)
    res.encoding = "utf-8"
    result = res.json()['data']['movie']
    try:
        suggested_url = 'https://yts.mx/api/v2/movie_suggestions.json?movie_id='+str(pk)
        suggested_res = requests.get(suggested_url)
        suggested_data = suggested_res.json()['data']['movies']
    except:
        suggested_data = None

    data = {
        'movie': result,
        'suggested_movies': suggested_data
    }
    return render(request, 'movies/details.html', data)


def latest_movies(request):
    return HttpResponse()


def popular_movies(request):
    sort_by = '&sort_by=download_count'
    url = "https://yts.mx/api/v2/list_movies.json"
    if request.GET.get('page'):
        url = url+"?page=" + request.GET.get('page')

    new_url = str(url+sort_by)

    res = requests.get(new_url)
    res.encoding = "utf-8"
    result = res.json()
    movies = result["data"]["movies"]
    data = {
        'movies': movies,
    }
    print(new_url)
    return render(request, 'all_movies.html', data)


def most_downloaded_movies(request):
    return HttpResponse('ok')