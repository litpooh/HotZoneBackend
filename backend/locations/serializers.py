from rest_framework import serializers
from locations.models import Location

class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=500, allow_blank=True)
    xcoord = serializers.FloatField()
    ycoord = serializers.FloatField()
    
    # allow_blank
    
    def create(self, validated_data):
        name = validated_data["name"]
        address = validated_data["address"]
        xcoord = validated_data["xcoord"]
        ycoord = validated_data["ycoord"]

        return Location.objects.get_or_create(name=name,address=address,xcoord=xcoord,ycoord=ycoord)[0]