# -*- coding: utf-8 -*-
# @Time    : 19-1-15 下午5:58
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : serializers.py
# @Software: PyCharm

from .models import Goods, GoodsCategory, GoodsImage
from rest_framework import serializers


class CategorySerializers3(serializers.ModelSerializer):
    '''
    商品分类序列化 类目３
    '''

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializers2(serializers.ModelSerializer):
    '''
    商品分类序列化　类目２
    '''
    sub_cat = CategorySerializers3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    '''
    商品分类序列化　类目１
    '''
    sub_cat = CategorySerializers2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsImageSerializers(serializers.ModelSerializer):
    '''
    商品图片序列化
    '''
    class Meta:
        model = GoodsImage
        fields = '__all__'


class GoodSerializers(serializers.ModelSerializer):
    '''
    商品列表序列化
    '''
    category = CategorySerializers()
    images = GoodsImageSerializers(many=True)

    class Meta:
        model = Goods
        fields = '__all__'
