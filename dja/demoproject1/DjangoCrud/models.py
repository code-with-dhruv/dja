from django.db import models

from django.db import models
from djongo import models

# Create your models here.
class Posts(models.Model):
    _id=models.ObjectIdField()
    StudentName=models.CharField(max_length=255)
    Age=models.CharField(max_length=2)
    DoB=models.CharField(max_length=255)
    Grade=models.CharField(max_length=255)
    objects=models.DjongoManager()
