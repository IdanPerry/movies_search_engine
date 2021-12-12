from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.db.models import Q
from psycopg2 import errors

from content import models
from content.forms import Search
from content.models import Movie
from content.movie import MovieContent
from content_data.models import MovieData
from services.drivers.solarmovie import Solarmovie
from services.drivers.moviesjoy import MoviesJoy

MAX_ITEMS = 42


def _retrieve_data() -> dict:
    # Retrieves the movie data from MovieData database model
    # and returns the data as a dictionary.

    data = MovieData.objects.all()
    data_dict = dict()
    for d in data:
        movie = MovieContent.by_data(d)
        data_dict[movie.title] = movie

    return data_dict


def insert(content) -> None:
    # Inserts the specified content into the database.

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


def _paginate(request, objects):
    paginator = Paginator(objects, MAX_ITEMS)
    page = request.GET.get('page')
    paged_objects = paginator.get_page(page)

    return paged_objects


def index(request):
    movies = Movie.objects.all()
    form = Search()

    context = {
        'paged_movies': _paginate(request, movies),
        'form': form
    }

    return render(request, 'index.html', context)


def search(request):
    form = Search()

    queryset_list = None

    if request.GET:
        title = request.GET.get('title')
        if not title:
            title = ''

        from_year = request.GET.get('from_year')
        if not from_year:
            from_year = 0

        to_year = request.GET.get('to_year')
        if not to_year:
            to_year = 2050

        from_rating = request.GET.get('from_rating')
        if not from_rating:
            from_rating = 0.0

        to_rating = request.GET.get('to_rating')
        if not to_rating:
            to_rating = 10.0

        actors = request.GET.get('actors')
        if not actors:
            actors = ''

        queryset_list = Movie.objects.filter(
            Q(title__icontains=title) & 
            Q(year__gte=from_year) & 
            Q(year__lte=to_year) &
            Q(rating__gte=from_rating) &
            Q(rating__lte=to_rating) &
            Q(actors__icontains=actors)
            )

    context = {
        'query_list': _paginate(request, queryset_list),
        'form': form,
    }

    return render(request, 'search.html', context)
