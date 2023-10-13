from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=128, 
        unique=True,
    )


class AppliedHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    applied_user = models.ForeignKey(
        "profiles.User",
        on_delete=models.CASCADE,
        related_name="applied_historys",
    )
    job_posting = models.ForeignKey(
        "jobs.JobPosting",
        on_delete=models.CASCADE,
        related_name="applied_historys",
    )