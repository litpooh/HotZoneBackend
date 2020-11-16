from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    idNumber = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    def __str__(self):
        return self.name