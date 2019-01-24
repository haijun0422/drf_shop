from django.shortcuts import render
# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # 添加访问权限
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import UserFav, UserLeavingMessage, UserAddress
from .serializers import UserFavSerializers, UserFavDetailSerializer, LeavingMsgSerializer, AddressSerializer
from utils.permission import IsOwnerOrReadOnly


class UserFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
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

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 添加访问权限,登录状态
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # 使用JWT token,session验证
    lookup_field = 'goods_id'

    def get_serializer_class(self):
        '''
        动态获取serializer
        :return:
        '''
        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == 'create':
            return UserFavSerializers
        return UserFavSerializers

    def get_queryset(self):
        '''重写get_queryset查询集'''
        return UserFav.objects.filter(user=self.request.user)


class LeavingMessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    '''
    list:
        获取留言
    create:
        增加留言
    delete:
        删除留言
    '''
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 添加访问权限,登录状态
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # 使用JWT token,session验证
    serializer_class = LeavingMsgSerializer

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    '''
    　收货地址
    list:
        获取收货地址
    create:
        增加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    '''
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 添加访问权限,登录状态
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # 使用JWT token,session验证

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
