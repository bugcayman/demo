# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render,reverse

# Create your views here.

"""
视图函数必须要有个参数,接收request(HTTPRequest)请求对象
视图函数必须要有响应对象 HttpResponse
"""

"""
定义路由的方式
总加子
子
总
"""
def index(request):
    reverse('users:index')
    return HttpResponse('hello world')
