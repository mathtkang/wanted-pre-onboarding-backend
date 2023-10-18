from rest_framework.serializers import ModelSerializer
from profiles.models import User, AppliedHistory
from jobs.models import Company, JobPosting
from jobs.serializers import JobPostingSerializer


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "is_company",
        )


# class CompanyProfileSerializer(ModelSerializer):
#     class Meta:
#         model = Company
#         fields = (
#             "name",
#             "country",
#             "location",
#         )