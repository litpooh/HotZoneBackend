from rest_framework import serializers
from .models import Virus

class VirusSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=20)
    # commonName = serializers.CharField(max_length=20)
    # maxInfectiousPeriod = serializers.IntegerField()

    class Meta:
        model = Virus
        fields = "__all__"

    def create(self, validated_data):
        return Virus.objects.get_or_create(**validated_data)[0]

    def update(self, instance, validated_data):
        pass