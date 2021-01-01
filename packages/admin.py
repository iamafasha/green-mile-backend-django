from django.contrib import admin
from .models import Package , ShippingLocation , Shipping , PackageSize


admin.site.register(Shipping)
admin.site.register(Package)
admin.site.register(ShippingLocation)
admin.site.register(PackageSize)