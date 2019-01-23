# -*- coding: utf-8 -*-
# @Time    : 19-1-23 下午2:17
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : permission.py
# @Software: PyCharm
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义用户验证
    当前用户操作
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
