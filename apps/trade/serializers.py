# -*- coding: utf-8 -*-
# @Time    : 19-1-24 下午3:27
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from .models import ShoppingCart
from goods.models import Goods


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label='数量', help_text='数量', min_value=1, error_messages={
        'min_value': '数量不能小于１',
        'required': '请选择数量',
    })
    goods = serializers.PrimaryKeyRelatedField(required=True, label='商品', help_text='商品', queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context['request'].user
        nums = validated_data['nums']
        goods = validated_data['goods']
        existed = ShoppingCart.objects.filter(user=user, goods=goods)
        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed
