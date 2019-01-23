from django.shortcuts import render
# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # 添加访问权限
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import UserFav
from .serializers import UserFavSerializers
from utils.permission import IsOwnerOrReadOnly


class UserFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    用户收藏功能
    收藏和取消收藏是一个添加和删除的过程
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    destroy:
        取消收藏
    '''
    serializer_class = UserFavSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 添加访问权限
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # JWT token,session
    lookup_field = 'goods_id'

    def get_queryset(self):
        '''重写get_queryset查询集'''
        return UserFav.objects.filter(user=self.request.user)
