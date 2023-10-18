from rest_framework.permissions import BasePermission, SAFE_METHODS


# user의 is_company=False 이면 '유저' 이고
# user의 is_company=True 이면 '회사' 이다.

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_company

class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_company

class IsAuthenticatedCompanyOrReadOnlyUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_company:
            # 사용자가 회사로 로그인한 경우 수정 권한을 허용
            return True
        # 읽기 전용 권한을 모든 다른 사용자에게 부여
        return request.method in SAFE_METHODS
