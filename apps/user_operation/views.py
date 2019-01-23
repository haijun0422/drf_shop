from django.shortcuts import render
# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from .models import UserFav
from .serializers import UserFavSerializers


class UserFavViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializers
