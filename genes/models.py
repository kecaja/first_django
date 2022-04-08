from tkinter import CASCADE
from django.db import models

# Create your models here.
class Gene(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Build(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField()

class Chromosone(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Interval(models.Model):
    start_coordinate = models.IntegerField()
    end_coordinate = models.IntegerField()
    gene = models.ForeignKey(Gene, on_delete=models.PROTECT, related_name='Interval')
    build = models.ForeignKey(Build, on_delete=models.PROTECT, related_name='Interval')
    chromosone = models.ForeignKey(Chromosone, on_delete=models.PROTECT, related_name='Interval')



    