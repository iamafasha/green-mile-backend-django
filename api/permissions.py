from rest_framework import permissions
from users.models import Worker

class IsWorker(permissions.BasePermission):
    message = "Login with Supplier Account"
    
    def has_object_permission(self, request, view, obj):
        try:
            user = Worker.objects.get(username=request.user)
        except Worker.DoesNotExist:
            return False
        return True
