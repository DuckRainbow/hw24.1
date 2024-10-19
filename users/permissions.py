from rest_framework import permissions

class IsModerator(permissions.BasePermission):
    message = 'Вы не являетесь модератором.'

    def has_permission(self, request, view):
         return request.user.groups.filter(name="moderator").exists()
