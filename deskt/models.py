from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed


class SmokeDetection(models.Model):
    Descp = models.CharField(max_length=10)
    date = models.DateField()
    frequency = models.IntegerField()
    # Other fields as needed

class WebsiteLink(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name

