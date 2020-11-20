from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Virus)
admin.site.register(CaseRecords)
admin.site.register(Patient)