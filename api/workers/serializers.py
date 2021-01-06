from api.serializers import serializers , PackageSizeSerializer, ShippingLocationSerializer , ShippingSerializer
from users.models import Supplier
from packages.models import Package , PackageSize , ShippingLocation , Shipping

class WorkerPackageSerializer(serializers.ModelSerializer):
    size = PackageSizeSerializer()
    to = ShippingSerializer()
    class Meta:
        model = Package
        fields = ['id','supplier', 'name', 'size', 'to', 'type', 'status' ]
        read_only_fields = ['id','supplier', 'name', 'size', 'to', 'type']