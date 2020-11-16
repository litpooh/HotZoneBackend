from django.db import models
from patient.models import Patient
from virus.models import Virus
from django.utils import timezone

# Create your models here.
class CaseRecord(models.Model):
    dateOfConfirm = models.DateField()
    localOrImported = models.CharField(max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.patient.name} {self.virus.name} (Case ID:{self.id})"