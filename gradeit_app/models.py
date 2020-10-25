from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = ImageField(blank=True, manual_crop="")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=60, blank=True)
    contact = models.IntegerField(blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


  

