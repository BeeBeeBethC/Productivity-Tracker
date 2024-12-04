from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class custom_user(models.Model):
    username = models.CharField(max_length=50, unique = True)
    firstname = models.Charfield(max_length=30)
    lastname = models.Charfield(max_length=30)
    email = models.Emailfield(unique = True)
    password = models.CharField(_('password'), max_length=128)
    is_staff = models.BooleanField(default = False)

    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'email', 'password']
    
    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
        ordering = ['email']

    def __str__(self):
        return self.email

class Tracker(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=128, unique=True)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}-{self.task}"

