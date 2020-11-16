from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def create(self, validated_data):
        return Patient.objects.get_or_create(**validated_data)[0]

    def update(self, instance, validated_data):
        pass