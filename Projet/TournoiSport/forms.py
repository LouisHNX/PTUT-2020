from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import tournament

class CreationUserFormulaire(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class TournamentForm(ModelForm):
    class Meta:
        model = tournament
        fields = ['name', 'sport', 'nb', 'place', 'date']