from rest_framework import serializers
from packages.models import  PackageSize , ShippingLocation , Shipping

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

