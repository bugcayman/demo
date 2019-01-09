from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def weather(request,city,year):
    print(city)
    print(year)
    return HttpResponse('weather1')



def weather2(request,city,year):
    print(city)
    print(year)
    return HttpResponse('weather2')

def query_par(request):

    query_parDict = request.GET
    print(query_parDict.get('a'))
    print(query_parDict.get('b'))
    print(query_parDict.getlist('a'))
    return HttpResponse('query_par')


def get_body_form(request):
    """岩石提示请求表但数据"""
    query_parDict = request.POST
    print(query_parDict.get('like'))
    print(query_parDict.get('b'))
    print(query_parDict.getlist('like'))

    return HttpResponse('get_body_form')


def get_body(request):
    a = request.POST.get('ln')
    b = request.POST.get('lne')
    list = request.POST.getlist('ln')
    print(a)
    print(b)
    print(list)
    return HttpResponse('OK')

def get_body_body(request):
    """提取请求体json数据"""
    json_str_bytes = request.body
    json_str = json_str_bytes.decode()
    json_data = json.loads(json_str)
    print(json_data['a'])
    print(json_data['b'])
    return HttpResponse('你好')