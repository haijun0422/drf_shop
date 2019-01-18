# -*- coding: utf-8 -*-
# @Time    : 19-1-18 下午6:19
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : task.py
# @Software: PyCharm

from apps.utils.yuntongxun.send_sms_code import sendTemplateSMS
from celery_tasks.main import app


@app.task(name="send_sms_code")
def send_sms_code(mobile, code, tmpId):
    sendTemplateSMS(mobile, {code, '5'}, tmpId)
