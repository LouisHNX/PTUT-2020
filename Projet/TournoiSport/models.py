from django.db import models

class team(models.Model):

    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class pool(models.Model):

    idPool = models.IntegerField()

class phase(models.Model):

    idPhase = models.IntegerField()
    typePhase = models.CharField(max_length = 50)
    nbTeamPerPool = models.IntegerField()
    nbTeamQualified = models.IntegerField()