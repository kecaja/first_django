from django.db import models

# Create your models here.
class Gene(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Build(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Chromosone(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Interval(models.Model):
    #name = models