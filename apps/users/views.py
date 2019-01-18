from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django_redis import get_redis_connection

from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from random import choice
from apps.utils.yuntongxun.send_sms_code import sendTemplateSMS
from .serializers import SmsSerializer
from celery_tasks.tasks import send_sms_code

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    '''
    发送短信验证码
    '''
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        print(random_str)

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        con = get_redis_connection('smscodes')
        flag = con.get('smscodes_flag_%s' % mobile)
        if flag:
            return Response({"error": "请求过于频繁"})
        code = str(self.generate_code())
        # 生成管道对像
        pl = con.pipeline()
        # 保存短信验证码到redis中
        pl.setex('smscodes_%s' % code, 300, code)
        # 设置请求时效标志
        pl.setex('smscodes_flag_%s' % mobile, 60, 1)
        # 执行管道(连接缓存，存入数据)
        pl.execute()
        # 调用云通讯发送短信
        # sendTemplateSMS(mobile, {self.generate_code(), '1'}, 1)
        # 使用celery异步发送短信
        send_sms_code.delay(mobile, code, 1)
        return Response({"message": "ok"})