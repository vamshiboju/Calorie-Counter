from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Calc(models.Model) :
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.FloatField() 
    res = models.FloatField()
    def _str_(self):
        return self.username
    
class Breakfast(models.Model):
    food_name =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    calories = models.FloatField()
    quantity = models.IntegerField()

class Lunch(models.Model):
    food_name =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    calories = models.FloatField()
    quantity = models.IntegerField()

class Dinner(models.Model):
    food_name =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    calories = models.FloatField()
    quantity = models.IntegerField()    
