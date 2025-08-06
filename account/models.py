from django.db import models
from django.contrib.auth.models import users

class UserProfile(models.model):
    user = models.OneTOOneField(user,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.user.username

# Create your models here.
