from django.db import models

# Create your models here.
class Virus(models.Model):
    name = models.CharField(max_length=20)
    commonName = models.CharField(max_length=20)
    maxInfectiousPeriod = models.IntegerField()
    def __str__(self):
        return self.name