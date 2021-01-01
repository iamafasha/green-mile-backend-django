from rest_framework import serializers
from users.models import Supplier

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ['company_name','company_domain', 'email', 'password']

