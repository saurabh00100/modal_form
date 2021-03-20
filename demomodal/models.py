from django.db import models

class Post(models.Model):
    titel=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    content=models.TextField()

