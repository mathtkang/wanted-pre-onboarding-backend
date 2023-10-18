from django.urls import path
from profiles import views

app_name = "profiles"

# url: v1/profiles/

urlpatterns = [
    path("login", views.LogIn.as_view()),  # 추가구현 not 요구사항
    path("logout", views.LogOut.as_view()),  # 추가구현 not 요구사항
    path("user", views.UserProfile.as_view()),  # 추가구현 not 요구사항
    # path("company", views.CompanyProfile.as_view()),  # 추가구현 not 요구사항
    path("applied", views.UserAppliedCompanies.as_view()),  # 추가구현 not 요구사항
]