from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username