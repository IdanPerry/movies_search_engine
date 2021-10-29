from django.contrib import admin

from .models import MovieData, Movie
from content.drivers.imdb import IMDb
from content.drivers.solarmovie import Solarmovie

# Register all models
admin.site.register(MovieData)
admin.site.register(Movie)

# Start all drivers threads
# IMDb(IMDb.CONTENT['movies']).start()
# Solarmovie(Solarmovie.CONTENT['movies']).start()
