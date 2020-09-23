from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    REQUIRED_FIELDS = [username, password, email]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'