from django.db import models
from django.contrib.auth.models import User

# Create your models here
class UserModel(models.Model):
    username = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    image = models.ImageField(null=False, blank=False)

class Statistics(models.Model):
    second = models.IntegerField(default=0)
    numberofdrowsy = models.IntegerField()
    timeofdrowsy = models.DateTimeField(auto_now_add=True, blank=True)
