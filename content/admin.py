from django.contrib import admin

from .models import MovieData, Movie
from content.drivers.imdb import IMDb
from content.drivers.solarmovie import Solarmovie


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'year', 'rating')
    list_display_links = ('id', 'title')
    list_filter = ('type',)
    search_fields = ('title', 'year', 'actors')
    list_per_page = 50


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'source')
    list_display_links = ('id', 'title')
    list_filter = ('type', 'source')
    search_fields = ('title',)
    list_per_page = 50


# Register all models
admin.site.register(MovieData, DataAdmin)
admin.site.register(Movie, MovieAdmin)

# Start all drivers threads
# IMDb(IMDb.CONTENT['movies']).start()
# Solarmovie(Solarmovie.CONTENT['movies']).start()
