from django.db import models

# Create your models here.

class Food(models.Model):
    Breakfast = models.CharField(max_length=200)
    Lunch = models.CharField(max_length=200)
    Dinner = models.CharField(max_length=200)