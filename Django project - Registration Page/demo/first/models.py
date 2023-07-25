from django.db import models

# Create your models here.
class Table(models.Model):
    name=models.CharField(max_length=120)
    Email=models.CharField(max_length=120)
    course=models.CharField(max_length=120)

