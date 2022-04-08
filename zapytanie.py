from datetime import datetime
from tkinter.messagebox import QUESTION
from genes.models import Gene, Build, Chromosone, Interval

Gene.objects.create('name_1')
Build.objects.create('name2', datetime(2020,1,1))
Chromosone.objects.create('name3')