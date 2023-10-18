from django import forms
from rest_framework.serializers import ModelSerializer, CharField, PrimaryKeyRelatedField, CurrentUserDefault, SerializerMethodField
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
            "companys",
            "position",
            "reward",
            "technologies"
        )
        pagination_class = PageNumberPagination


class TinyCompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "name",
        )

class JobPostingCreateSerializer(ModelSerializer):
    companys = TinyCompanySerializer(read_only=True)
    class Meta:
        model = JobPosting
        fields = (
            "companys",
            "position",
            "reward",
            "description", 
            "technologies",
        )
    
