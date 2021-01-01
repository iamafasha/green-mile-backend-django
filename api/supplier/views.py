from rest_framework import viewsets
from rest_framework.decorators import action
from users.models import Supplier
from .serializers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('-date_joined')
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['patch', 'delete'])
    def unset_password(self, request, pk=None):
        pass