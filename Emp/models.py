from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name= models.CharField(max_length=15, verbose_name="Enter ur name : ")
    last_name= models.CharField(max_length=15)   
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)   


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title
