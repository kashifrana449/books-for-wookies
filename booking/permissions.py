from rest_framework.permissions import BasePermission


class BookingPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated and request.user.first_name.lower() == 'darth' and request.user.last_name.lower() == 'vader':
            return False
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user == obj.author:
            return True
