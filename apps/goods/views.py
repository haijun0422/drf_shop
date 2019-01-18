from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from .models import Goods, GoodsCategory
from .serializers import GoodSerializers, CategorySerializers
from .filters import GoodsFilters
from django_filters.rest_framework import DjangoFilterBackend


class SetPagination(PageNumberPagination):
    '''分页'''
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    商品展示,分页,过滤,搜索,排序
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodSerializers  # 商品展示
    pagination_class = SetPagination  # 分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤,搜索,排序
    filter_class = GoodsFilters
    filter_fields = ('name', 'goods_desc')  # 过滤
    search_fields = ('name', 'goods_brief', 'goods_brief')  # 搜索
    ordering_fields = ('click_num', 'shop_price')  # 排序


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    商品分类列表
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializers
