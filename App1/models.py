from django.db import models


class Regions(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Cities(models.Model):
    cname = models.CharField(max_length=45)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

class Attractions(models.Model):
    names = models.CharField(max_length=50)
    city = models.OneToOneField(Cities, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    description = models.TextField()
    dateoffoundation = models.DateField()
    saving = models.BinaryField(default=False)

    def __str__(self):
        return self.names

