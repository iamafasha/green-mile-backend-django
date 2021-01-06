from api.serializers import serializers , PackageSizeSerializer, ShippingLocationSerializer , ShippingSerializer
from packages.models import Package , ShippingLocation ,PackageSize, Shipping

class PackageSerializer(serializers.ModelSerializer):
    size = PackageSizeSerializer()
    to = ShippingSerializer()
    class Meta:
        model = Package
        fields = ['id','supplier', 'name', 'size', 'to', 'type', 'status']
    
    def create(self, validated_data):
        size_data= validated_data.pop('size')
        receiver_data = validated_data.pop('to')
        location = receiver_data.pop('location')
        # Create the related objects
        location = ShippingLocation(**location)
        location.save()
        to=Shipping(location=location, **receiver_data)
        to.save()

        size=PackageSize(**size_data)
        size.save()
        return Package.objects.create( to=to, size=size , **validated_data)