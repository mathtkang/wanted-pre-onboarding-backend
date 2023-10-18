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
from jobs.serializers import JobPostingListSerializer, JobPostingCreateSerializer, JobPostingDetailsSerializer, JobPostingSerializer
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
        raise NotFound("채용 공고를 찾을 수 없습니다.")
    
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
                detail="해당 요청에 맞는 채용공고를 찾을 수 없습니다."
            )

        return queryset


class JobPostingDetails(APIView):
    '''
    🔗 url: /jobs/<int:jpid>
    '''
    permissions_classes = [IsAuthenticatedCompanyOrReadOnlyUser]

    def get_jp_object(self, jpid):
        try:
            return JobPosting.objects.get(id=jpid)
        except JobPosting.DoesNotExist:
            raise NotFound(
                detail="해당 채용공고를 찾을 수 없습니다."
            )

    def get(self, request, jpid):
        '''
        구체적인 채용공고 목록 반환
        ✅ distcription 포함
        ✅ 해당 회사의 또 다른 채용공고도 반환
        '''
        job_posting = self.get_jp_object(jpid)
        serializer = JobPostingDetailsSerializer(job_posting)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK,
        )

    def put(self, request, jpid):
        '''
        ✅ 해당 회사만 채용공고 수정할 수 있도록
        '''
        if not request.user.is_authenticated:
            return Response(
                {'detail': '로그인 이후에 채용공고 수정할 수 있습니다.'},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if not request.user.is_company:
            return Response(
                {'detail': '유저는 채용공고를 수정할 수 없습니다.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        job_posting = self.get_jp_object(jpid)

        # if request.user.company in job_posting.companys.all():  # 쿼리셋에 포함되어 있는 경우로 구현해도 됨
        if request.user.company == job_posting.companys.first():
            serializer = JobPostingSerializer(
                job_posting, 
                data=request.data,
                partial=True,
            )

            if serializer.is_valid():
                updated_job_posting = serializer.save()
                return Response(
                    JobPostingSerializer(updated_job_posting).data,
                    status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                    {'detail': '수정 권한이 없습니다.'},
                    status=status.HTTP_403_FORBIDDEN,
                )
            

    def delete(self, request, jpid):
        '''
        ✅ 해당 회사만 채용공고 삭제할 수 있도록
        '''
        if not request.user.is_authenticated:
            return Response(
            {'detail': '로그인 이후에 채용공고를 삭제할 수 있습니다.'},
            status=status.HTTP_401_UNAUTHORIZED,
        )
        if not request.user.is_company:
            return Response(
                {'detail': '유저는 채용공고를 삭제할 수 없습니다.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        job_posting = self.get_jp_object(jpid)

        if request.user.company == job_posting.companys.first():
            job_posting.delete()
            return Response(
                {'detail': '채용공고가 삭제되었습니다.'},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {'detail': '삭제 권한이 없습니다.'},
                status=status.HTTP_403_FORBIDDEN,
            )



class ApplyToJob(APIView):
    '''
    🔗 url: /jobs/<int:jpid>/apply
    '''
    def get_jp_object(self, jpid):
        try:
            return JobPosting.objects.get(id=jpid)
        except JobPosting.DoesNotExist:
            raise NotFound(
                detail="해당 채용공고를 찾을 수 없습니다."
            )

    def post(self, request, jpid):
        '''
        ✅ 유저만 지원할 수 있음
        ✅ 한번 지원한 채용공고는 다시 지원 불가
        '''
        if not request.user.is_authenticated:
            return Response(
                {'detail': '로그인한 사용자만 채용공고를 지원할 수 있습니다.'},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if request.user.is_company:
            return Response(
                {'detail': '회사는 채용공고를 지원할 수 없습니다.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        job_posting = self.get_jp_object(jpid)

        # 이미 지원한 경우
        if AppliedHistory.objects.filter(
            applied_user=request.user, 
            job_posting=job_posting
        ).exists():
            return Response(
                {'detail': '이미 이 채용공고에 지원하였습니다.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        applied_history = AppliedHistory(
            applied_user=request.user, 
            job_posting=job_posting
        )
        applied_history.save()

        return Response(
            {'detail': '채용공고에 성공적으로 지원하였습니다.'},
            status=status.HTTP_201_CREATED,
        )

