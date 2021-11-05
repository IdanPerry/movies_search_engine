from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.utils import IntegrityError
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from psycopg2 import errors
from contextlib import suppress

from content import models
from content.models import Movie
from services.drivers.solarmovie import Solarmovie
from services.drivers.moviesjoy import MoviesJoy

MAX_ITEMS = 90

def insert(id, content, source, content_type):
    with suppress(errors.lookup('23505'), IntegrityError):
        movie = models.Movie(id=id, title=content.name, type=content_type, source=source,
                            url=content.url, image=content.image)
        movie.save()

def test(request):
    solar = Solarmovie(Solarmovie.CONTENT['movies'])
    solar.start()
    solar.join()
    movies = solar.get_content()

    id = 0
    for movie in movies:
        id += 1
        insert(id, movie, 'Solarmovie', 'movie')

    joy = MoviesJoy(MoviesJoy.CONTENT['movies'])
    joy.start()
    joy.join()
    movies = joy.get_content()

    for movie in movies:
        id += 1
        insert(id, movie, 'MoviesJoy', 'movie')

    return HttpResponse('')

def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, MAX_ITEMS)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)

    context = {
        'paged_movies': paged_movies
    }

    return render(request, 'index.html', context)
