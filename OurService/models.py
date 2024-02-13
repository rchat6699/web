from django.db import models
class ServiceModel(models.Model):
    ourserviceTitle=models.TextField()
    iconImg=models.TextField()
    titleName=models.TextField()
    descMessage=models.TextField()
    readmoreLink=models.TextField()


# Create your models here.
