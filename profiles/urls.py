from django.urls import path
from profiles import views

app_name = "profiles"

# url: v1/profiles/

urlpatterns = [
    path("login", views.LogIn.as_view()),
    path("logout", views.LogOut.as_view()),
    path("user", views.UserProfile.as_view()),
    path("company", views.CompanyProfile.as_view()),
]