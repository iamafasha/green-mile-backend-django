from rest_framework import viewsets , generics , status 
from users.models import Supplier 
from packages.models import Package
from .serializers import SupplierSerializer, SupplierPackageSerializer
from rest_framework.permissions import IsAuthenticated

class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer

class SupplierPackageViewSet(generics.ListCreateAPIView ):
    serializer_class = SupplierPackageSerializer
    queryset = Package.objects.all()
    permission_classes = [IsAuthenticated ]

    def get_queryset(self):
        return Package.objects.filter(supplier=self.request.user)

class SupplierPackageDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SupplierPackageSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Package.objects.filter(supplier=self.request.user)
    
