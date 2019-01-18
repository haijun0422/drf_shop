# -*- coding: utf-8 -*-
# @Time    : 18-12-26 下午3:08
# @Author  : Nick
# @Email   : haijun0422@126.com
# @File    : storage.py
# @Software: PyCharm

from django.core.files.storage import Storage
from django.conf import settings

from fdfs_client.client import Fdfs_client


class FDFSStorage(Storage):
    '''
    自定义fdfs文件储存类
    必须重写 _open() 和 _save()方法 (http://doc.codingdict.com/django/howto/custom-file-storage.html)
    还需要重写 exsits()和url() 方法
    '''

    def __init__(self, client_conf=None, base_url=None):
        '''初始化'''
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_BASE_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self, name, content):
        '''保存文件时使用，这是fdfs文件存储的关键'''
        # 创建Fsfs_client类,参数是client.conf文件的路径
        client = Fdfs_client(self.client_conf)
        # 上传文件到fastdfs系统中
        res = client.upload_by_buffer(content.read())
        print(res)

        '''
        res返回的是一个字典
        {
            'Group name': group_name,
            'Remote file_id': remote_file_id,
            'Status': 'Upload successed.',
            'Local file name': '',
            'Uploaded size': upload_size,
            'Storage IP': storage_ip
        }
        '''
        if res.get('Status') != 'Upload successed.':
            # 上传文件失败
            raise Exception('文件上传失败')
        # 获取返回文件的ID
        filename = res.get('Remote file_id')
        # print(filename)
        # print(os.path.dirname(filename))

        return filename

    def exists(self, name):
        '''
        如果提供的名称所引用的文件在文件系统中存在，则返回True，否则如果这个名称可用于新文件，返回False。
        '''
        return False

    def url(self, name):
        '''
        返回URL，通过它可以访问到name所引用的文件
        nginx地址+文件名 <img http://192.168.211.130:8888/name />
        '''
        # return 'http://192.168.211.130:8888/'+name
        return self.base_url + name
