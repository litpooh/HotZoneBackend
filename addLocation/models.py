from django.db import models
from viewCases.models import CaseRecord
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, null=True)
    xcoord = models.FloatField()
    ycoord = models.FloatField()

    def __str__(self):
        return self.name


class VisitedLocation(models.Model):
    dateFrom = models.DateField()
    dateTo = models.DateField()
    category = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    caseRecord = models.ForeignKey(CaseRecord, on_delete=models.CASCADE)

    def __str__(self):
        return self.location.name + ", " + self.dateFrom.strftime("%Y-%m-%d") + " to " + self.dateTo.strftime("%Y-%m-%d")
