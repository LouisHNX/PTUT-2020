from django.db import models
from django import forms

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
        return self.tournament


