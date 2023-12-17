from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from django.contrib.auth.models import AbstractUser



class ResourceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    resource_type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Note(Resource):
    content = models.TextField()

class Ebook(Resource):
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    file = models.FileField(upload_to='ebooks/')

class Link(Resource):
    url = models.URLField()

class Video(Resource):
    file = models.FileField(upload_to='videos/')

class Image(Resource):
    image_file = models.ImageField(upload_to='images/', verbose_name='Image File')

class Document(Resource):
    file = models.FileField(upload_to='documents/')


    




