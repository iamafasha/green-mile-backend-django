from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSupplier(BasePermission):
    message = "Use supllier account"
    
    def has_object_permission(self, request, view, obj):
        return False
        
    def has_permission(self, request, view):
        return False