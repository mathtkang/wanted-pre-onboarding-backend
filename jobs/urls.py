from django.urls import path
from jobs import views

app_name = "jobs"

# url: v1/jobs/

urlpatterns = [
    path("", views.JobPostingList.as_view()),
]