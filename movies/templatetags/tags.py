import requests
from django import template

register = template.Library()


@register.simple_tag
def popular_movies():
    sort_by = '&sort_by=download_count'
    url = "https://yts.mx/api/v2/list_movies.json?limit=8&sort_by=like_count"

    new_url = str(url)

    res = requests.get(new_url)
    res.encoding = "utf-8"
    result = res.json()
    movies = result["data"]["movies"]
    data = {
        'movies': movies,
    }
    return data