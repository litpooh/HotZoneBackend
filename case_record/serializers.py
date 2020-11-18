from rest_framework import serializers
from .models import CaseRecord
from virus.models import Virus
from patient.serializers import PatientSerializer
from virus.serializers import VirusSerializer

class CaseRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    virus = VirusSerializer()
    class Meta:
        model = CaseRecord
        fields = ('dateOfConfirm', 'localOrImported', 'patient',  'virus')

    def create(self, validated_data):
        patient_serializer = self.fields['patient']
        virus_serializer = self.fields['virus']
        dateOfConfirm = validated_data['dateOfConfirm']
        localOrImported = validated_data['localOrImported']

        patient = patient_serializer.create(validated_data['patient'])
        virus = virus_serializer.create(validated_data['virus'])

        case_record = CaseRecord.objects.create(patient=patient,virus=virus,dateOfConfirm=dateOfConfirm,localOrImported=localOrImported)

        return case_record

class CreateCaseRecordSerializer(serializers.Serializer):
    patient = PatientSerializer()
    dateOfConfirm = serializers.DateField()
    localOrImported = serializers.CharField(max_length=20)
    virus = serializers.CharField(max_length=20)

    def create(self, validated_data):
        dateOfConfirm = validated_data['dateOfConfirm']
        localOrImported = validated_data['localOrImported']

        virusName = validated_data['virus']
        virusObj = Virus.objects.get(name=virusName)

        patient_serializer = self.fields['patient']
        patient = patient_serializer.create(validated_data['patient'])

        case_record = CaseRecord.objects.create(patient=patient,virus=virusObj,dateOfConfirm=dateOfConfirm,localOrImported=localOrImported)

        return case_record


class ViewCaseSerializer(serializers.Serializer):
    dateOfConfirm = serializers.DateField()
    localOrImported = serializers.CharField(max_length=20)
    patient = PatientSerializer()
    virus = VirusSerializer()

    def create(self, validated_data):
        return validated_data