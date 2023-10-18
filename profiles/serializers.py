from rest_framework.serializers import ModelSerializer
from profiles.models import User
from jobs.models import Company


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username"
        )
        # fields = "__all__"


class CompanyProfileSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "name",
            "country",
            "location",
        )
        # fields = "__all__"
