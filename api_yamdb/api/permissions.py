from rest_framework import permissions


class PermissionsOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return (
                obj.owner == request.user
                or request.user.role == 'MODERATOR'
                or request.user.role == 'ADMIN'
            )
