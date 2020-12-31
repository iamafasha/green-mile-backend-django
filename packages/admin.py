from django.contrib import admin
from .models import Package , ShippingLocation , Shipping , PackageSize



class PackageAdmin(admin.ModelAdmin):
    pass

class ShippingAdmin(admin.ModelAdmin):
    pass  

class ShippingLocationAdmin(admin.ModelAdmin):
    pass

class PackageSizeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(ShippingLocation, ShippingLocationAdmin)
admin.site.register(PackageSize , PackageSizeAdmin)