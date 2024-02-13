from django.db import models
class EmpModel(models.Model):
    teamTitle=models.TextField()
    teamImg=models.TextField()
    employeeName=models.TextField()
    designation=models.TextField()
# Create your models here.
