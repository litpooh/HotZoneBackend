from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from locations.models import Location
from rest_framework.parsers import JSONParser
from locations.serializers import LocationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class LocationView(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        # location = self.kwargs['']
        context = super().get_context_data(**kwargs)
        context['location_list'] = Location.objects.all()
        return context





