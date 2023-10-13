from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_posting = models.ManyToManyField('JobPosting', related_name='companys')


class JobPosting(models.Model):
    position = models.CharField(max_length=256)
    reward = models.PositiveIntegerField()
    description = models.TextField()
    technologies = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)