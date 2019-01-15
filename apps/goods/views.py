from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from .serializers import GoodSerializers


class GoodsView(APIView):
    '''
    商品展示
    '''

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_json = GoodSerializers(goods, many=True)
        return Response(goods_json.data)
