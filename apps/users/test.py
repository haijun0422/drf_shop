# -*- coding: utf-8 -*-
# @Time    : 19-1-18 下午5:49
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : test.py
# @Software: PyCharm

def generate_code():
    """
    生成四位数字的验证码
    :return:
    """
    seeds = "1234567890"
    random_str = [code for code in seeds for i in range(4)]
    print(random_str)

    return "".join(random_str)

if __name__ == '__main__':

    generate_code()