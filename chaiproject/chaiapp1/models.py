from django.db import models

# Create your models here.
class Users(models.Model):
    CONTINENT_CHOICES = [
        ('africa', 'africa'),
        ('asia', 'asia'),
        ('australia', 'australia'),
        ('europe', 'europe'),
        ('north_america', 'north_america'),
        ('south_america', 'south_america'),
    ]
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.CharField(max_length=100, default="no description")
    profilepic = models.ImageField(upload_to='profilepics/')
    continent = models.CharField(max_length=50, choices=CONTINENT_CHOICES)
