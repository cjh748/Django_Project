from django.db import models
from django.db.models import CASCADE


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
