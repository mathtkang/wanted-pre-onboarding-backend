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


class JobPostingSerializer(ModelSerializer):
    class Meta:
        model = JobPosting
        fields = (
            "id",
            "position",
            "reward",
            "description",
            "technologies",
        )

class JobPostingDetailsSerializer(ModelSerializer):
    companys = CompanySerializer(many=True, read_only=True)
    other_job_postings = SerializerMethodField()
    
    class Meta:
        model = JobPosting
        fields = (
            "id",
            "companys",
            "position",
            "description",
            "technologies",
            "reward",
            "other_job_postings",  # add field
        )
    
    def get_other_job_postings(self, obj):
        other_job_postings = JobPosting.objects.filter(
            companys__in=obj.companys.all()
        ).exclude(
            id=obj.id
        )
        return other_job_postings.values_list('id', flat=True)