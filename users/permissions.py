from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import IsAdminUser

class IsAdmin(BasePermission):
   
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser



class IsCooperativeOfficial(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'cooperative_official'


class IsFarmer(BasePermission):  
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'farmer'



    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.user_type == 'cooperative_official':
            return True
        return request.method in SAFE_METHODS and hasattr(obj, 'farmer') and obj.farmer == request.user