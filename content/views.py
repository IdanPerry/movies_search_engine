from django.shortcuts import render
from django.db.utils import IntegrityError
from psycopg2 import errors
from contextlib import suppress

from content import models


def insert_data(content, content_type):
    with suppress(errors.lookup('23505'), IntegrityError):
        data = models.MovieData(title=content.name, type=content_type, year=content.year, rating=content.rating,
                                description=content.description, actors=content.actors, trailer=content.trailer)
        data.save()


def insert_show(content, source, content_type):
    with suppress(errors.lookup('23505'), IntegrityError):
        show = models.Movie(title=content.name, type=content_type, source=source, link=content.link)
        show.save()
