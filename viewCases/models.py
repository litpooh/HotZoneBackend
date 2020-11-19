from django.db import models
from django.utils import timezone

# Create your models here.
class Virus(models.Model):
    name = models.CharField(max_length=20)
    commonName = models.CharField(max_length=20)
    maxInfectiousPeriod = models.IntegerField()
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    idNumber = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    def __str__(self):
        return self.name
class CaseRecord(models.Model):
    dateOfConfirm = models.DateField()
    localOrImported = models.CharField(max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.patient.name} {self.virus.name} (Case ID:{self.id})"

