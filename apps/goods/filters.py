# -*- coding: utf-8 -*-
# @Time    : 19-1-17 下午1:37
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : filters.py
# @Software: PyCharm

from .models import Goods
from django.db.models import Q
import django_filters


class GoodsFilters(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot']
