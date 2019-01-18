# -*- coding: utf-8 -*-
# @Time    : 19-1-18 下午6:23
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : main.py
# @Software: PyCharm

'''
celery　启动文件
'''
from celery import Celery

# 为celery使用django配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'drf_shop.settings'

# 创建celery应用
app = Celery('drf_shop')

# 导入celery配置
app.config_from_object('celery_tasks.config')

# 自动注册celery任务
app.autodiscover_tasks(['celery_tasks.sms'])