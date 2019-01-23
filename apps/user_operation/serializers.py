# -*- coding: utf-8 -*-
# @Time    : 19-1-23 下午1:25
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav


class UserFavSerializers(serializers.ModelSerializer):
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