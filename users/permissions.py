from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Проверяет, является ли пользователь модератором.
    """
    message = 'Вы не являетесь модератором.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsCreator(permissions.BasePermission):
    """
    Проверяет, является ли пользователь создателем.
    """

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
