from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.parsers import JSONParser

from addresses.models import Addresses
from addresses.serializers import AddressesSerializer


@csrf_exempt
def address_list(request):
    if request.method == 'GET': # 데이터 조회
        query_set = Addresses.objects.all() # addresses 객체 모두 가져옴
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST': # 데이터 생성
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # 객체 생성
            return JsonResponse(serializer.data, status=201) # 성공
        return JsonResponse(serializer.errors, status=400) # 실패