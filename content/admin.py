from django.contrib import admin
from content.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'rating', 'type', 'source')
    list_display_links = ('id', 'title')
    list_filter = ('type', 'source')
    search_fields = ('title',)
    list_per_page = 50


admin.site.register(Movie, MovieAdmin)
