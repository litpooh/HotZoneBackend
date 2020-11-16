from django.db import models
from locations.models import Location
from case_record.models import CaseRecord

# Create your models here.
class VisitedLocation(models.Model):
    dateFrom = models.DateField()
    dateTo = models.DateField()
    category = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    caseRecord = models.ForeignKey(CaseRecord, on_delete=models.CASCADE)
    def __str__(self):
        return self.location.name +" "+ self.dateFrom.strftime("%Y-%m-%d") + " to " + self.dateTo.strftime("%Y-%m-%d")