from django.db import models
class AboutModel(models.Model):
    aboutusTitle=models.TextField()
    iconImg=models.TextField()
    titleName=models.TextField()
    descMessage=models.TextField()
    readmoreLink=models.TextField()
# Create your models here.
