# -*- coding: utf-8 -*-
# @Time    : 19-1-15 下午5:58
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers


class GoodSerializers(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=50)
    click_num = serializers.IntegerField(default=0)
