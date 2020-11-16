from rest_framework import serializers
from .models import VisitedLocation
from locations.models import Location
from locations.serializers import LocationSerializer
from case_record.models import CaseRecord
from case_record.serializers import CaseRecordSerializer

class VisitedLocationSerializer(serializers.Serializer):
    location = LocationSerializer()
    # CaseRecord = CaseRecordSerializer()
    # class Meta:
    #     model = VisitedLocation
    #     fields = ('dateFrom', 'dateTo', 'category','location','caseID')

    dateFrom = serializers.DateField()
    dateTo = serializers.DateField()
    category = serializers.CharField(max_length=20)
    caseID = serializers.IntegerField()

    def validate_caseID(self, value):
        return value

    def create(self, validated_data):
        dateFrom = validated_data['dateFrom']
        dateTo = validated_data['dateTo']
        category = validated_data['category']
        location_serializer = self.fields['location']
        # case_record_serializer = self.fields['case_record']

        location = location_serializer.create(validated_data['location'])
        # print(validated_data)
        caseID = validated_data['caseID']
        case_record = CaseRecord.objects.get(id=caseID)
        
        visited_location = VisitedLocation.objects.create(dateFrom=dateFrom,dateTo=dateTo,category=category,location=location,caseRecord=case_record)

        return visited_location

