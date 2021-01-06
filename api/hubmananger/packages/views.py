from rest_framework import viewsets , generics
from packages.models import Package
from .serializers import PackageSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsHubMananger



class PackageViewSet(generics.ListCreateAPIView , IsHubMananger ):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()
    permission_classes = ( IsAuthenticated , IsHubMananger )

class PackageDetailViewSet(generics.RetrieveUpdateDestroyAPIView , IsHubMananger):

    serializer_class = PackageSerializer
    permission_classes = (IsAuthenticated, IsHubMananger )
    lookup_field = "id"

    def get_queryset(self):
        return Package.objects.all()
    
