from django.conf.urls import url

from . import  views


urlpatterns = [
    # 演示提取url路径参数,位置参数
    url(r'^weather/([a-z]+)/(\d{4})/$',views.weather),
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$',views.weather2),
    url(r'^query_par/$',views.query_par),
    url(r'^get_body_form/$',views.get_body_form),
    url(r'^get_body/$',views.get_body),
    url(r'^get_body_non_form/$',views.get_body_non_form),
    url(r'^get_headers/$',views.get_headers),
    url(r'^response_demo/$',views.response_demo),
    url(r'^json_response_demo/$',views.json_response_demo,name='index'),
    url(r'^redirect_demo/$',views.redirect_demo),
    url(r'^cookie_demo/$',views.cookie_demo),
]

