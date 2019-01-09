from django.conf.urls import url

from . import  views


urlpatterns = [
    # 演示提取url路径参数,位置参数
    url(r'^weather/([a-z]+)/(\d{4})/$',views.weather),
]