from django import forms
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.pagination import PageNumberPagination
from jobs.models import Company, JobPosting


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "name",
            "country",
            "location",
        )


class JobPostingListSerializer(ModelSerializer):
    companys = CompanySerializer(many=True, read_only=True)
    class Meta:
        model = JobPosting
        fields = (
            "id",
            "companys",  # Company 모델의 속성이 여기에 포함됩니다.
            "position",
            "reward",
            "technologies"
        )
        pagination_class = PageNumberPagination
