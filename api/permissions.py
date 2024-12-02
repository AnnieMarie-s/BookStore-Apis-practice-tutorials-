
from rest_framework import permissions
from django.contrib.auth.models import User

class isownerOrreadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return  bool(request.user or request.user.is_staff)
        
class isownerOrreadonlyobject(permissions.BasePermission):
        
    def has_object_permission(self, request, view, obj):
        if request.method in  permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.user
