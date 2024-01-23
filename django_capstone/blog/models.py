from django.db import models


# Create your models here.
class Post(models.Model):
    """
    A class to represent a post
    ...
    Atrributes
    ----------
    id : int
    title : str
    body :
    date :
    signature : 
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()
    signature = models.CharField(max_length=200)

def __str__(self):
    return self.title