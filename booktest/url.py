from django.conf.urls import url

from . import  views

urlpatterns = [
    url(r'^books/$',views.BooksAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BooksView.as_view()),
]