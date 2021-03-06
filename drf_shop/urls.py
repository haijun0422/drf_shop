"""drf_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
import xadmin
from django.conf import settings
from django.views.static import serve

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset, UserRegisterViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet

router = DefaultRouter()
router.register(r'^goods', GoodsListViewSet, base_name='goods')  # 商品列表
router.register(r'^categorys', CategoryViewSet, base_name='categorys')  # 商品分类
router.register(r'code', SmsCodeViewset, base_name='code')  # 短信验证码
router.register(r'users', UserRegisterViewSet, base_name='users')  # 用户注册
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')  # 用户收藏
router.register(r'messages', LeavingMessageViewSet, base_name='messages')  # 用户留言
router.register(r'address', AddressViewSet, base_name='address')  # 收货地址
router.register(r'shopcarts', ShoppingCartViewSet, base_name='shopcarts')  # 收货地址

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # 登录rest_framework
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'editor/', include('DjangoUeditor.urls')),
    url(r'doc/', include_docs_urls(title='电商系统')),

    # url(r'^goods/', GoodsView.as_view()),
    url('', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),  # drf自带的token认证模式
    url(r'^login/', obtain_jwt_token),  # JWT 用户认证接口
]
