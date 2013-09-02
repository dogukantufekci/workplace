# from rest_framework import permissions


# class IsPersonOwnerOrReadOnly(permissions.BasePermission):
#     # def has_permission(self, request, view):
#     #   return request.user.is_staff

#     def has_object_permission(self, request, view, obj):
#         if obj.user is None or obj.user == request.user:
#             return True

#         return request.method in permissions.SAFE_METHODS


# class IsWikiAdminOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user in obj.admins.all():
#             return True

#         return request.method in permissions.SAFE_METHODS