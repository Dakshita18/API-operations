from django.db import models
from django.utils.text import slugify




class product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    Description = models.TextField(max_length=400)
    Image = models.URLField()  # easier to store image URLs
    category = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    zipcode = models.CharField(max_length=20)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=5)
    version = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.username})"

























































