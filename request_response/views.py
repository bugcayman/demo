from django.shortcuts import render,reverse,redirect

from django.http import HttpResponse, HttpResponseBadRequest,JsonResponse

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

def get_body_non_form(request):
    """提取请求体json数据"""
    json_str_bytes = request.body
    json_str = json_str_bytes.decode()
    json_data = json.loads(json_str)


    print(json_data)
    print(request.user)

    return HttpResponse('你好')

def get_headers(request):
    print(request.META['CONTENT_TYPE'])
    return HttpResponse('OK')

def response_demo(request):


    # return HttpResponse(content="nihao",content_type="text/html",status=200)
    response = HttpResponse('python')
    response['it'] = 'haha'
    # HttpResponseBadRequest
    return response

def json_response_demo(request):
    """演示json"""
    # dict_json = {'name':'zs','age':18}
    json_list1 = [{'name':'zs','age':18},{'name':'zs','age':18}]

    # 如果用JsonResponse响应的不是一个字典时,需要设置safe=False
    return JsonResponse(json_list1,safe=False)



def redirect_demo(request):
    #反响解析:通过视图找路由
    #正像解析:通过路由找视图
    print(reverse('request_response:index'))
    return HttpResponse('redirect_demo')


def cookie_demo(request):
    """掩饰cookie操作"""
    response = HttpResponse('cookie_demo')
    response.set_cookie("name","chaoge",60*60)#设置key和value都必须是字符串类型
    print(request.COOKIES.get('name'))

    return response

