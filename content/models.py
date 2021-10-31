from django.db import models

TYPE = [
    ('movie', 'movie'),
    ('tv-show', 'tv-show')
]


class Movie(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TYPE)
    source = models.CharField(max_length=30)
    url = models.CharField(max_length=300)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title
