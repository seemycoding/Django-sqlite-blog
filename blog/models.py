from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class AddPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    titile=models.CharField(max_length=50)
    category=models.CharField(max_length=25)
    body=models.CharField(max_length=255)

    def __str__(self):
        return self.titile
    
    


       



