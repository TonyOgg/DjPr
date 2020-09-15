from django.db import models

# Create your models here.

class Regions(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=15)

class Cities(models.Model):
    cname = models.CharField(max_length=45)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)

