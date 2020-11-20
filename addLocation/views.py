from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VisitedLocation
from .serializers import VisitedLocationSerializer
from django.views.generic import TemplateView
from .retrieveLocation import searchAndCompareLocation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateVisitedLocationAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = VisitedLocationSerializer(data=request.data)
        if serializer.is_valid():
            visitedLocation = serializer.save()
            return Response(visitedLocation.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateVisitedLocationView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = "create_visited_location.html"

    def get_context_data(self, **kwargs):
        return

class LocationView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
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
