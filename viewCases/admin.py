from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Virus)
admin.site.register(CaseRecord)
admin.site.register(Patient)