from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


class UserNetPublicView(viewsets.ModelViewSet):
    """Вывод публичного профиля пользователя"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(viewsets.ModelViewSet):
    """Вывод профиля пользователя"""
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
