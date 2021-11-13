from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from psycopg2 import errors

from content import models
from content.models import Movie
from content.movie import MovieContent
from content_data.models import MovieData
from services.drivers.solarmovie import Solarmovie
from services.drivers.moviesjoy import MoviesJoy

MAX_ITEMS = 90


def _retrieve_data() -> dict:
    # Retrieves the movie data from MovieData databass model
    # and returns the data as a dictionary.

    data = MovieData.objects.all()
    data_dict = dict()
    for d in data:
        movie = MovieContent.by_data(d)
        data_dict[movie.title] = movie

    return data_dict


def insert(content) -> None:
    # Inserts the specified content into the databass.

    try:
        movie = models.Movie(title=content.title, type=content.type, year=content.year, rating=content.rating,
                             description=content.description, actors=content.actors, trailer=content.trailer,
                             url=content.url, image=content.image, source=content.source,
                             )
        movie.save()
    except (errors.lookup('23505'), IntegrityError) as e:
        print(e)


def import_content(request) -> HttpResponse:
    # importing movies with services.drivers tools.

    movie_parsers = set()
    drivers = [
        Solarmovie(Solarmovie.MOVIES),
        MoviesJoy(MoviesJoy.MOVIES),
    ]

    for driver in drivers:
        driver.start()

    data = _retrieve_data()

    for driver in drivers:
        driver.join()
        movie_parsers = movie_parsers.union(driver.get_content())

    movies = {MovieContent.by_content(m) for m in movie_parsers}
    counter = 0
    
    for movie in movies:
        try:
            movie.merge(data[movie.title])
            insert(movie)
        except KeyError as e:
            print(f'{e} is not in movie_data database')
            counter += 1

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
