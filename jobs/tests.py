from rest_framework import status
from rest_framework.test import APITestCase

from profiles.models import User, AppliedHistory
from jobs.models import Company, JobPosting


BASE_URL="/v1/jobs"

class TestJobPostingDetails(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", 
            password="testpassword"
        )
        self.company = Company.objects.create(
            name="원티드랩", 
            country="한국", 
            location="서울"
        )
        self.jobposting = JobPosting.objects.create(
            position="백엔드 개발자",
            reward=500000,
            description="원티드에서 구직자가 쉽고 빠르게 원하는 포지션을 찾고 지원하여 합격까지 이어질 수 있도록 AI를 통한 합격률 높은 포지션 추천, 이력서 분석 가이드 등 채용 전반에 걸친 서비스를 개발하는 채용 스쿼드와 전국 240만 개 기업의 공공 데이터, 오픈 데이터를 가공하여 구직자에게 유용한 기업 정보를 제공할 수 있도록 원티드인사이트를 개발하는 인사이트 스쿼드로 구성되어 있습니다.",
            technologies="Python",
        )
        self.jobposting.companys.add(self.company)

    def tearDown(self):
        self.user.delete()
        self.company.delete()
        self.jobposting.delete()

    # [jpid로 찾는 JobPosting이 없는 경우]
    def test_get_jp_object(self):
        response = self.client.get(f"{BASE_URL}/2")
        self.assertEqual(
            response.status_code,
            404
        )
    
    # [jpid로 찾는 JobPosting이 있는 경우]
    def test_get(self):
        response = self.client.get(f"{BASE_URL}/1")
        self.assertEqual(
            response.status_code, 
            200
        )
        data = response.json()
        self.assertEqual(
            data["position"],
            "백엔드 개발자",
        )
        self.assertEqual(
            data["reward"],
            500000,
        )

    def test_delete(self):
        response = self.client.delete(
            f"{BASE_URL}/2",
        )
        self.assertEqual(
            response.status_code, 
            404
        )

        JobPosting.objects.create(
            position="백엔드 개발자",
            reward=500000,
            description="원티드에서 구직자가 쉽고 빠르게 원하는 포지션을 찾고 지원하여 합격까지 이어질 수 있도록 AI를 통한 합격률 높은 포지션 추천, 이력서 분석 가이드 등 채용 전반에 걸친 서비스를 개발하는 채용 스쿼드와 전국 240만 개 기업의 공공 데이터, 오픈 데이터를 가공하여 구직자에게 유용한 기업 정보를 제공할 수 있도록 원티드인사이트를 개발하는 인사이트 스쿼드로 구성되어 있습니다.",
            technologies="Python",
        )
        response = self.client.delete(
            f"{BASE_URL}/2",
        )
        self.assertEqual(
            response.status_code, 
            403
        )