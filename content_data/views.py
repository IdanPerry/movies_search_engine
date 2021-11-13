from django.http.response import HttpResponse
from django.db.utils import IntegrityError
from psycopg2 import errors

from content_data import models
from services.drivers.imdb import IMDb


def insert(content):
    try:
        data = models.MovieData(title=content.name, type=content.type, year=content.year, rating=content.rating,
                                description=content.description, actors=content.actors, trailer=content.trailer)
        data.save()
    except (errors.lookup('23505'), IntegrityError) as e:
        print(e)


def import_data(request) -> HttpResponse:
    # imports movies data with services.drivers tools.

    driver = IMDb(IMDb.MOVIES)
    driver.start()
    driver.join()
    movies = driver.get_content()

    for movie in movies:
        movie.type = 'movie'
        insert(movie)

    return HttpResponse('')
