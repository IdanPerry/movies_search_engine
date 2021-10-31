from django.shortcuts import render
from django.db.utils import IntegrityError
from psycopg2 import errors
from contextlib import suppress

from content_data import models


def insert(content, content_type):
    with suppress(errors.lookup('23505'), IntegrityError):
        data = models.MovieData(title=content.name, type=content_type, year=content.year, rating=content.rating,
                                description=content.description, actors=content.actors, trailer=content.trailer)
        data.save()
