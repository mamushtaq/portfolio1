from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Websites(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to = 'images')
    link = models.TextField(max_length=1229, default=None)
    title = models.TextField(max_length=128)
    description = models.TextField(max_length=1000)

class Graphics(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField()
    title = models.TextField(max_length=128)
    description = models.TextField(max_length=1000)

class Videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to = 'images')
    link = models.TextField(max_length=1229, default=None)
    title = models.TextField(max_length=128)
    description = models.TextField(max_length=1000)