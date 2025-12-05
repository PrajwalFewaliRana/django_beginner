from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo= models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100,unique=True)
    #blank = True means phonenumber is optional
    phone_number = models.CharField(max_length=12,blank=True)
    
    #auto_now_add = True for one time created and modification and saved for the first time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)