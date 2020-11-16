from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from visited_location.models import VisitedLocation
from visited_location.serializers import VisitedLocationSerializer
from django.views.generic import TemplateView

# Create your views here.
class CreateVisitedLocationAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = VisitedLocationSerializer(data=request.data)
        if serializer.is_valid():
            visitedLocation = serializer.save()
            return Response(visitedLocation.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateVisitedLocationView(TemplateView):
    template_name = "create_visited_location.html"

    def get_context_data(self, **kwargs):
        return