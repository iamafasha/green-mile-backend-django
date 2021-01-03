from rest_framework import serializers
from users.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['username','company_name','company_domain', 'email', 'password']

