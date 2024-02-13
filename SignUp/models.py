from django.db import models

# Create your models here.
class Signupform(models.Model):
    Email=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    RepeatPassword=models.CharField(max_length=150)