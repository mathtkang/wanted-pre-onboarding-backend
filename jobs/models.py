from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256, unique=True,)  # 회사명
    country = models.CharField(max_length=256)  # 회사국가
    location = models.CharField(max_length=256)  # 회사지역
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_posting = models.ManyToManyField('JobPosting', related_name='companys')


class JobPosting(models.Model):
    position = models.CharField(max_length=256)  # 채용포지션
    reward = models.PositiveIntegerField()  # 채용보상금
    description = models.TextField()  # 채용내용
    technologies = models.CharField(max_length=256)  # 사용기술
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)