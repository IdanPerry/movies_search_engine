from django.db import models

TYPE = [
    ('movie', 'movie'),
    ('tv-show', 'tv-show')
]


class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=7, choices=TYPE)
    year = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    actors = models.CharField(max_length=300, blank=True, null=True)
    trailer = models.CharField(max_length=300, blank=True, null=True)
    url = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    source = models.CharField(max_length=30)

    def __str__(self):
        return self.title
