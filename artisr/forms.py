from django import forms
from .models import Album, Musician
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AddSongForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'release_date', 'num_stars', 'song_lyrics' ]

class AddSingerForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name','instrument']


