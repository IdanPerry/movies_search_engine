from django.contrib import admin

from content.models import Movie
from services.drivers.solarmovie import Solarmovie
from services.drivers.moviesjoy import MoviesJoy


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'source')
    list_display_links = ('id', 'title')
    list_filter = ('type', 'source')
    search_fields = ('title',)
    list_per_page = 50


admin.site.register(Movie, MovieAdmin)
# Solarmovie(Solarmovie.CONTENT['movies']).start()
# MoviesJoy(MoviesJoy.CONTENT['movies']).start()
