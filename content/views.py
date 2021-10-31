from django.shortcuts import render
from django.db.utils import IntegrityError
from psycopg2 import errors
from contextlib import suppress

from content import models


def insert(content, source, content_type):
    with suppress(errors.lookup('23505'), IntegrityError):
        show = models.Movie(title=content.name, type=content_type, source=source,
                            url=content.url, image=content.image)
        show.save()


def index(request):
    return render(request, 'index.html')
