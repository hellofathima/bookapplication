from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.IntegerField()
    publisher=models.CharField(max_length=200)
    category=models.CharField(max_length=200)

    def __str__(self): 
        return self.title