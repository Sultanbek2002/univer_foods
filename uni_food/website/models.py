from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
class ClientUser(AbstractUser):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to='media/userPhoto/%Y/%m/%d',null=True)
    birth_day=models.TextField(max_length=50)
    login=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    about_self=models.TextField()
    phone=PhoneNumberField(blank=True)
    passport_photo_up=models.ImageField(upload_to='media/passport/%Y/%m/%d', null=True)
    passport_photo_down=models.ImageField(upload_to='media/passport/down/%Y/%m/%d',null=True)
    status_user=models.CharField(default='viewer',max_length=40,null=True)
    

