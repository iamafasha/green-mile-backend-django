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


class IsHubMananger(permissions.BasePermission):
    message = "You must be a hub mananger to perform this action"
    
    def has_object_permission(self, request, view, obj):
        try:
            user = Worker.objects.get(username=request.user)
            if(user.is_hub_manager is False):
                return False
        except Worker.DoesNotExist:
            return False
        return True

    def has_permission(self, request, view):
        try:
            user = Worker.objects.get(username=request.user)
            if(user.is_hub_manager is False):
                return False
        except Worker.DoesNotExist:
            return False
        return True