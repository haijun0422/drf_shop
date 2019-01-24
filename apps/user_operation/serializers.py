# -*- coding: utf-8 -*-
# @Time    : 19-1-23 下午1:25
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav, UserLeavingMessage, UserAddress
from goods.serializers import GoodSerializers


class UserFavDetailSerializer(serializers.ModelSerializer):
    '''
    用户收藏详情序列化类
    '''
    goods = GoodSerializers()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class UserFavSerializers(serializers.ModelSerializer):
    '''
    用户收藏序列化类
    '''
    user = serializers.HiddenField(  # 获取当前用户，覆盖user
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已经收藏'
            )
        ]
        model = UserFav
        fields = ('user', 'goods', 'id')


class LeavingMsgSerializer(serializers.ModelSerializer):
    '''
    用户留言序列化类
    '''
    user = serializers.HiddenField(  # 获取当前用户，覆盖user
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ('id', 'user', 'message_type', 'subject', 'message', 'file', 'add_time')


class AddressSerializer(serializers.ModelSerializer):
    '''
    用户收货地址序列化类
    '''
    user = serializers.HiddenField(  # 获取当前用户，覆盖user
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ('id', 'user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time')

