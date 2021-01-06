from rest_framework import generics 
from packages.models import Package
from .serializers import WorkerPackageSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsWorker

class WorkerPackageDetailViewSet(generics.RetrieveUpdateDestroyAPIView, IsWorker):

    serializer_class = WorkerPackageSerializer
    permission_classes = (IsWorker, IsAuthenticated)
    lookup_field = "id"

    def get_queryset(self):
        return Package.objects.all()
    
