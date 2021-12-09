from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student_Table(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    age=models.IntegerField()
    dob=models.DateField()
    place=models.CharField(max_length=30)

class facebook(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=25)
    email=models.CharField(max_length=20)
    password=models.IntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=10)



# facebook 2
class facebook2(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email_mobile=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    # re_password=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    file=models.CharField(max_length=200)

    
    
    
class facebookform(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.CharField(max_length=30)
    password=models.IntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    file=models.CharField(max_length=200)

        # imgfile model
class imgfile(models.Model):
    name=models.CharField(max_length=40)
    file=models.CharField(max_length=150)


# ajax2 model
class ajax2(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=50)












# ORM_Login Demo
class Orm_login_Demo(models.Model):
    UserName=models.CharField(max_length=30)
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.CharField(max_length=25)
    Mobile=models.CharField(max_length=12)
    Password1=models.CharField(max_length=30)
    Password2=models.CharField(max_length=30)


class api(models.Model):
    username=models.CharField(max_length=20)
    password=models.IntegerField()








