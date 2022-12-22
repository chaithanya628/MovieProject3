from django import forms;
from Movieapp.models import Movies

class MoviesForm(forms.ModelForm):
    #no-separate fields are required(taken from model-Movies-class)
    class Meta:
        model = Movies
        fields = ('releasedate', 'moviename', 'actor', 'actress', 'rating');

