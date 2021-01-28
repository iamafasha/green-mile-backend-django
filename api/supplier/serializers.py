from api.serializers import serializers , PackageSizeSerializer, ShippingLocationSerializer , ShippingSerializer
from users.models import Supplier
from packages.models import Package , ShippingLocation , Shipping , PackageSize


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id','username','company_name','company_domain', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user 

class SupplierPackageSerializer(serializers.ModelSerializer):
    size = PackageSizeSerializer()
    to = ShippingSerializer()
    class Meta:
        model = Package
        fields = ['id','supplier', 'name', 'size', 'to', 'type', 'status']
        read_only_fields = ['supplier' , 'status']
    
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