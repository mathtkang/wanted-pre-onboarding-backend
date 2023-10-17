import os
import requests
import json

from django.core.paginator import Paginator, EmptyPage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from jobs.models import Company, JobPosting
from jobs.serializers import JobPostingListSerializer
from profiles.models import User, AppliedHistory



class CustomPagination(PageNumberPagination):
    page_size = 20  # 한 페이지당 표시할 항목 수
    page_size_query_param = 'page_size'  # URL에서 페이지 크기를 설정하기 위한 쿼리 파라미터
    max_page_size = 1000  # 최대 페이지 사이즈


class JobPostingList(ListAPIView):
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
