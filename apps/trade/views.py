from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permission import IsOwnerOrReadOnly
from .serializers import ShoppingCartSerializer, ShoppingCartDetailSerializer
from .models import ShoppingCart


class ShoppingCartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 添加访问权限,登录状态
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # 使用JWT token,session验证
    serializer_class = ShoppingCartSerializer
    lookup_field = 'goods_id'  # 商品id

    def get_serializer_class(self):
        '''
        动态获取serializer
        :return:
        '''
        if self.action == 'list':
            return ShoppingCartDetailSerializer
        elif self.action == 'create':
            return ShoppingCartSerializer
        return ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)