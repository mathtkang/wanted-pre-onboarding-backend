from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from config.permissions import IsAuthenticatedCompanyOrReadOnlyUser

from jobs.models import Company, JobPosting
from jobs.serializers import JobPostingListSerializer, JobPostingCreateSerializer, JobPostingDetailsSerializer
from profiles.models import User, AppliedHistory


class CustomPagination(PageNumberPagination):
    page_size = 20  # 한 페이지당 표시할 항목 수
    page_size_query_param = 'page_size'  # URL에서 페이지 크기를 설정하기 위한 쿼리 파라미터
    max_page_size = 1000  # 최대 페이지 사이즈


class JobPostingList(ListCreateAPIView):
    '''
    🔗 url: /jobs/?page=n
    ✅ 모든 채용공고 목록 반환
    ✅ pagination(page=20) 적용
    '''
    permissions_classes = [AllowAny]

    queryset = JobPosting.objects.all()
    if not queryset.exists():
        raise NotFound
    serializer_class = JobPostingListSerializer
    pagination_class = CustomPagination

    def create(self, request):
        '''
        ✅ 채용공고 등록 : 회사만 가능 
        '''
        user = request.user
        if not user.is_company:
            return Response(
                {'detail': '회사 계정만 채용공고를 등록할 수 있습니다.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        # company_id = request.data.get("company_id")  # company_id로 구분해도 됨
        company_name = request.data.get("company_name")
        if not company_name:
            return Response(
                {'detail': '회사를 지정해야 합니다. 회사이름을 함께 작성해주세요.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            company = Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            return Response(
                {'detail': '지정된 회사가 존재하지 않습니다.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = JobPostingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(companys=[company])
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST,
        )


class SearchJobPostingList(ListAPIView):
    '''
    🔗 url: /jobs/search?keyword=검색키워드&page=n
    ✅ 채용공고 '키워드 검색' 기능 (query param)
    ✅ pagination(page=20) 적용
    '''
    permissions_classes = [AllowAny]

    serializer_class = JobPostingListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword", "")

        queryset = JobPosting.objects.filter(
            Q(position__icontains=keyword)
            | Q(technologies__icontains=keyword)
            | Q(companys__name__icontains=keyword)
        ).distinct()

        if queryset.count() == 0:
            raise NotFound(
                detail="Not found any Job Posting matching your request."
            )

        return queryset


class JobPostingDetails(APIView):
    '''
    🔗 url: /jobs/<int:jpid>
    '''
    permissions_classes = [IsAuthenticatedCompanyOrReadOnlyUser]

    def get_pill_object(self, jpid):
        try:
            return JobPosting.objects.get(id=jpid)
        except JobPosting.DoesNotExist:
            raise NotFound(
                detail="This Job Posting Not Found."
            )

    def get(self, request, jpid):
        '''
        구체적인 채용공고 목록 반환
        ✅ distcription 포함
        ✅ 해당 회사의 또 다른 채용공고도 반환
        '''
        job_posting = self.get_pill_object(jpid)
        serializer = JobPostingDetailsSerializer(job_posting)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK,
        )