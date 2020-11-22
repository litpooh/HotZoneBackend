from django.contrib import admin
from .models import *


class CaseRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'dateOfConfirm', 'virus', 'localOrImported')
    search_fields = ['patient__name', 'dateOfConfirm']
    list_filter = ['dateOfConfirm']


admin.site.register(Virus)
admin.site.register(CaseRecord, CaseRecordAdmin)
admin.site.register(Patient)
