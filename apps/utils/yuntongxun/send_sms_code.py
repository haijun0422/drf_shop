# -*- coding: utf-8 -*-
# @Time    : 19-1-18 下午3:36
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : send_sms_code.py
# @Software: PyCharm

from utils.yuntongxun.CCPRestSDK import REST
# 主帐号
accountSid = '8a216da8679811d10167982347180008'

# 主帐号Token__init__.py
accountToken = '6f98bd7a728547b9aacbbe4ff8dc747e'

# 应用Id
appId = '8a216da8679811d101679823478c000f'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id
def sendTemplateSMS(to, datas, tempId):
    # 初始化REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    for k, v in result.items():

        if k == 'templateSMS':
            for k, s in v.items():
                print('%s:%s' % (k, s))
        else:
            print('%s:%s' % (k, v))


# sendTemplateSMS(手机号码,内容数据,模板Id)
if __name__ == '__main__':
    sendTemplateSMS('mobile', {'3306', '5'}, 1)  # 格式 3306表示验证码，5表示过期时间
