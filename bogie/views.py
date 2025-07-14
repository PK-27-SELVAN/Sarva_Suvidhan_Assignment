from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BogieInspection
from .serializers import BogieInspectionSerializer

class BogieInspectionViewSet(viewsets.ModelViewSet):
    queryset = BogieInspection.objects.all()
    serializer_class = BogieInspectionSerializer
