# -*- coding: utf-8 -*-
# @Time    : 19-1-18 下午5:19
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : serializers.py
# @Software: PyCharm
from django.contrib.auth import get_user_model
from django.conf import settings
from django_redis import get_redis_connection

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, min_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")
        # 验证手机号码是否合法
        if not re.match(settings.REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")
        return mobile


class RegisterSerializers(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码需要4位数字",
                                     "min_length": "验证码需要4位数字"
                                 },
                                 help_text="验证码")
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True)

    class Meta:
        model = User
        fields = ['username', 'code', 'mobile', 'password']

    def validate(self, attrs):
        # 短信验证
        # 1、获取reids中真实短信
        conn = get_redis_connection('smscodes')
        # rel_sms_mobile = conn.get("%s" % attrs['mobile'])
        rel_sms_code = conn.get("%s" % attrs['code'])
        # print(rel_sms_mobile)
        # 2、 判断验证码是否存在
        # if not rel_sms_mobile:
        #     raise serializers.ValidationError('验证码不存在')
        # 3、判断短信是否超过有效期
        if not rel_sms_code:
            raise serializers.ValidationError('短信验证码失效')
        # 4、比对用户输入的短信和redis中真实短信
        if attrs['code'] != rel_sms_code.decode():
            raise serializers.ValidationError('短信验证不一致')

        return attrs

    def create(self, validated_data):
        # 删除验证后的无验证码
        del validated_data['code']
        # 使用模型类保存
        validated_data['mobile'] = validated_data['username']
        user = User.objects.create_user(**validated_data)
        return user
