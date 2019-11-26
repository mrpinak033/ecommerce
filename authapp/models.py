from django.db import models


# Create your models here.
class SignUp(models.Model):
    uname = models.CharField(primary_key=True,max_length=10)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    dob = models.DateField()
    mobno = models.IntegerField()
    email = models.EmailField(max_length=30)
    pwd = models.CharField(max_length=10)
    cpwd = models.CharField(max_length=10)




