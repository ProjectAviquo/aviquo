from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    
class Category(models.Model):
    name = models.CharField(max_length=255)

#parent model
class Forum(models.Model):
    username=models.CharField(max_length=200,default="anonymous")
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    parent_post = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
class Opportunity(models.Model):
    name = models.CharField(max_length=200, default="hi")
    description = models.CharField(max_length=300)
    class Meta:
        managed  = True
        db_table = 'users_opportunity'
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return str(self.id)

class Waitlist(models.Model):
    email  = models.EmailField(max_length=70,blank=True,unique=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.id)
