from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        if view.basename in ["post"]:
            return bool(request.user and
                        request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        print(request.user)  # Check the user object in the request
        print(request.method)  # Check the request method
        print(view.basename)
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        if view.basename in ["post-comment"]:
            return bool(request.user and request.user.is_authenticated)
        return False