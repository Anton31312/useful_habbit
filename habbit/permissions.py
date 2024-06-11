from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = 'Доступ запрещен. Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Доступ запрещен. Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
    