from django.shortcuts import render
from django.db.utils import IntegrityError
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from psycopg2 import errors
from contextlib import suppress

from content import models
from content.models import Movie

MAX_ITEMS = 90

def insert(content, source, content_type):
    with suppress(errors.lookup('23505'), IntegrityError):
        show = models.Movie(title=content.name, type=content_type, source=source,
                            url=content.url, image=content.image)
        show.save()


def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, MAX_ITEMS)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)

    context = {
        'paged_movies': paged_movies
    }

    return render(request, 'index.html', context)
