from rest_framework import viewsets , generics
from users.models import Supplier
from packages.models import Shipping
from api.serializers import ShippingSerializer
from api.supplier.serializers import SupplierSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsHubMananger



class SupplierViewSet(generics.ListCreateAPIView , IsHubMananger ):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = ( IsAuthenticated , IsHubMananger )

class SupplierDetailViewSet(generics.RetrieveUpdateDestroyAPIView , IsHubMananger):

    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, IsHubMananger )
    lookup_field = "id"

    def get_queryset(self):
        return Supplier.objects.all()
    
class SupplierReceiversViewSet(generics.ListCreateAPIView , IsHubMananger ):
    serializer_class = ShippingSerializer
    permission_classes = ( IsAuthenticated , IsHubMananger )
    
    def get_queryset(self):
        supplier = Supplier.objects.get(pk=self.kwargs.get('id'))
        return Shipping.objects.filter(package__supplier=supplier)
