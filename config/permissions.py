from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and not request.user.is_company

class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.is_company

class IsAuthenticatedCompanyOrReadOnlyUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        if not request.user.is_anonymous and request.user.is_company:
            return True
        return False