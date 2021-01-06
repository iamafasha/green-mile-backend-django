from rest_framework import serializers
from users.models import Supplier
from packages.models import Package , PackageSize , ShippingLocation , Shipping

class ShippingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= ShippingLocation
        fields = ['latitude','longitude']

class PackageSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model= PackageSize
        fields = ['length', 'width' ,'height' ,'weight']

class ShippingSerializer(serializers.ModelSerializer):
    location = ShippingLocationSerializer()
    class Meta:
        model = Shipping
        fields = [
            'first_name', 
            'last_name',
            'phone_number',
            'email',
            'street_address',
            'village',
            'district',
            'country',
            'location'
            ]



class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['username','company_name','company_domain', 'email', 'password']

class SupplierPackageSerializer(serializers.ModelSerializer):
    size = PackageSizeSerializer()
    to = ShippingSerializer()
    class Meta:
        model = Package
        fields = ['id','supplier', 'name', 'size', 'to', ]
        read_only_fields = ['supplier']
    
    def create(self, validated_data):
        user =Supplier.objects.get(username=self.context['request'].user)
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
        return Package.objects.create(supplier=user, to=to, size=size , **validated_data)