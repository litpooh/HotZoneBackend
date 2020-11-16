from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from virus.serializers import VirusSerializer

# Create your views here.
class CreateVirusView(TemplateView):
    template_name = "create_virus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreateVirusAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = VirusSerializer(data=request.data)
        if serializer.is_valid():
            virus = serializer.save()
            return Response(virus.name, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
