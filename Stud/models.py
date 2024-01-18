from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Student(models.Model):
    first_name= models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)    
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30) 

    def __str__(self):
        return "%s %s"%(self.first_name,self.last_name)

class Student_Details(models.Model):
    stud_id = models.BigAutoField(primary_key=True)
    first_name= models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)    
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30) 
    
    
class User(AbstractUser):
    usertype = models.CharField(max_length=50)  
    phone=models.BigIntegerField(default=1)   

class Stud_user(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department= models.CharField(max_length=15)    
    plus_mark=models.IntegerField()
