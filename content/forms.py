from django import forms
from django.forms.widgets import TextInput

from content.models import Movie


class Search(forms.Form):
    title = forms.CharField(max_length=200, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    from_year = forms.IntegerField(required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Release Year (from)'}))
    to_year = forms.IntegerField(required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Release Year (to)'}))
    from_rating = forms.FloatField(required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'IMDb Rating (from)'}))
    to_rating = forms.FloatField(required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'IMDb Rating (to)'}))
    actors = forms.CharField(max_length=300, required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Staring Actors'}))
