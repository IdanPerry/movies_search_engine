from django.db import models

TYPE = [
    ('movie', 'movie'),
    ('tv-show', 'tv-show')
]


class MovieData(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TYPE, default='movie')
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    actors = models.CharField(max_length=300)
    trailer = models.CharField(max_length=300)

    class Meta:
        unique_together = (('title', 'year'),)

    def __str__(self):
        return self.title
