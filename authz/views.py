from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from authz.serializers import UserSerializer
from authz.models import User
import django_filters.rest_framework

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('username',)
