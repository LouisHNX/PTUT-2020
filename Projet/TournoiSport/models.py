from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class team(models.Model):

    idTeam = models.IntegerField()
    name = models.CharField(max_length = 50)
    idPoolT = models.IntegerField()

    def __str__(self):
        return self.name

class pool(models.Model):

    idPool = models.IntegerField()

class phase(models.Model):

    idPhase = models.IntegerField() #1 = phase de poule
    typePhase = models.CharField(max_length = 50)
    nbTeamPerPool = models.IntegerField()
    nbTeamQualified = models.IntegerField()

    def __str__(self):
        return self.typePhase

class tournament(models.Model):

    idTournament = models.IntegerField()
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
#TEST ->
class SettingsBackend(BaseBackend):
    def authenticate(self,request, username=None, password=None):
        login_valid =(settings.USER_LOGIN == username)
        pwd_valid = check_password(password,settings.USER_PASSWORD)