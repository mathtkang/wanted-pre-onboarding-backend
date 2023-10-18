from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.db.models import query

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from profiles.models import User
from jobs.models import Company, JobPosting
from config.permissions import IsUser, IsCompany, IsAuthenticatedCompanyOrReadOnlyUser


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")

        if not username:
            raise ParseError
        
        user = User.objects.filter(username=username).first()
        
        if user:
            login(request, user)
            return Response(
                {"detail": "로그인 되었습니다."},
                status=HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "해당 유저는 존재하지 않습니다."},
                status=HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"detail": "로그아웃 되었습니다."}, 
            status=HTTP_200_OK,
        )

