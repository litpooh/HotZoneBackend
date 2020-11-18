from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from locations.models import Location
from rest_framework.parsers import JSONParser
from locations.serializers import LocationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from locations.retrieveLocation import searchAndCompareLocation
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class LocationView(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        # location = self.kwargs['']
        context = super().get_context_data(**kwargs)
        context['location_list'] = Location.objects.all()
        return context


class LocationWithMatchOnTopView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        locations = searchAndCompareLocation(request.data['keyword'])
        if locations != -1:
            return Response(locations, status=status.HTTP_200_OK)
        return Response(locations, status=status.HTTP_400_BAD_REQUEST)




