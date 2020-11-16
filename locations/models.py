from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, null=True)
    xcoord = models.FloatField()
    ycoord = models.FloatField()
    def __str__(self):
        return self.name