from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
from _datetime import datetime

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        db_table = 's_user_fav'
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")  # 联合唯一，同一商品收藏多次时，会显示"字段 user, goods 必须能构成唯一集合。"，而不会出现多条记录

    def __str__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, verbose_name="用户")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                       help_text=u"留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)")
    subject = models.CharField(max_length=100, default="", verbose_name="主题")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 's_messages'
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User, verbose_name="用户", help_text='用户')
    province = models.CharField(max_length=100, default="", verbose_name="省份", help_text='省份')
    city = models.CharField(max_length=100, default="", verbose_name="城市", help_text='城市')
    district = models.CharField(max_length=100, default="", verbose_name="区域", help_text='地区')
    address = models.CharField(max_length=100, default="", verbose_name="详细地址", help_text='地址')
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人", help_text='签收人')
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话", help_text='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='时间')

    class Meta:
        db_table = 's_address'
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
