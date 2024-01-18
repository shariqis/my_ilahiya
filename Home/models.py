from django.db import models

# Create your models here.

class Student(models.Model):
    first_name= models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)    
    class Meta:
        db_table="tblStud"
        

class Employee(models.Model):
    first_name= models.CharField(max_length=15, verbose_name="Enter ur name : ")
    last_name= models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)   
    deprtm = (
        ('HR', 'Humen Resourse'),
        ('CS', 'Computer science'),
        ('EC', 'Electronics and Commun'),
    )      
    deprt = models.CharField(max_length=2, choices=deprtm)
    class Meta:
        db_table="tbl_emp"
        

    
        