from django.contrib import admin
from .models import AfashaUser , Supplier



class AfashaUserAdmin(admin.ModelAdmin):
    pass

class SupplierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(AfashaUser, AfashaUserAdmin)
