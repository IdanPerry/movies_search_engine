from django.contrib import admin

from content_data.models import MovieData
from services.drivers.imdb import IMDb
from services.drivers.solarmovie import Solarmovie
from services.drivers.moviesjoy import MoviesJoy


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'year', 'rating')
    list_display_links = ('id', 'title')
    list_filter = ('type',)
    search_fields = ('title', 'year', 'actors')
    list_per_page = 50


admin.site.register(MovieData, DataAdmin)
# IMDb(IMDb.CONTENT['movies']).start()
