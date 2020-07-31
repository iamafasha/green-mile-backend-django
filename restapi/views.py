from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PackageSerializer
from .models import Package
# Create your views here.

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all().order_by('name')
    serializer_class = PackageSerializer