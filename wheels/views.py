from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import WheelInspection
from .serializers import WheelInspectionSerializer

class WheelInspectionViewSet(viewsets.ModelViewSet):
    queryset = WheelInspection.objects.all()
    serializer_class = WheelInspectionSerializer
