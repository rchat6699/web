from django.db import models

# Create your models here.
class Subscribe(models.Model):
    fullname=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    message=models.TextField()
    
