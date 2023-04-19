from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .szs import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from card.models import PublicCardInfo
from card.szs import PublicCardInfoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAdminUser]


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublicCardDetail(RetrieveAPIView):
    queryset = PublicCardInfo.objects.all()
    serializer_class = PublicCardInfoSerializer


class PublicCardUpdateView(UpdateAPIView):
    serializer_class = PublicCardInfoSerializer
    queryset = PublicCardInfo.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PublicCardCreateView(CreateAPIView):
    serializer_class = PublicCardInfoSerializer
    queryset = PublicCardInfo.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
