#定义子路由应用自己的所有路由
from django.conf.urls import url,include
from . import views

urlpatterns = [
    #共两个参数(url正则,视图函数名)
    # url(r'^index/$', views.index),

    url(r'users/index/$', views.index),


]