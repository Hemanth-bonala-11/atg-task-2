from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime
from django import forms
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone_no=models.CharField(max_length=15)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
         return self.message

class Details(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    profile_pic = models.ImageField(upload_to="media/pictures/%Y",blank=True,null=True)
    username = models.CharField(max_length=122,primary_key=True)
    mailid = models.EmailField()
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    lane1 = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    pincode = models.IntegerField()
    type=models.CharField(max_length=12)

    def __str__(self):
        return self.username

class Blogs(models.Model):
    uniqueid=models.CharField(primary_key=True,max_length=255,auto_created=True)
    username=models.CharField(max_length=122)
    title=models.CharField(max_length=122)
    image=models.ImageField(upload_to='media/blog_images')
    category=models.CharField(max_length=122)
    summary=models.CharField(max_length=122)
    content=models.TextField()

    def __str__(self):
        return self.uniqueid
class Draft(models.Model):
    username = models.CharField(max_length=122,primary_key=True)
    title = models.CharField(max_length=122)
    image = models.ImageField(upload_to='media/blog_images')
    category = models.CharField(max_length=122)
    summary = models.CharField(max_length=122)
    content = models.TextField()
    def __str__(self):
        return self.username


