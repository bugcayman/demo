from django.shortcuts import render
# Create your views here.
import json
from django.views import View
from django.http import HttpResponse,JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from booktest.models import BookInfo



# book = BookInfo()
# book.btitle='西游记'
# book.bpub_date='1988-1-1'
# book.save()

# book = BookInfo(
#     btitle='红楼梦',
#     bpub_date='2000-11-11'
# )
# book.save()
# book = BookInfo.objects.create(
#     btitle='三国志',
#     bpub_date='2019-11-11'
# )
# hero = HeroInfo.objects.create(
#     hname =  '孙悟空',
#     hbook_id= 6,
#     hgender='1',
#     hcomment='大师兄,人帅功夫好'

# )
# hero = HeroInfo.objects.create(
#     hname =  '沙武警',
#     hbook_id= 6,
#     hgender='1',
#     hcomment='任劳任怨',
# )
# hero = HeroInfo.objects.create(
#     hname =  '猪八戒',
#     hbook_id= 6,
#     hgender='1',
#     hcomment='贪吃好色'
# )
# BookInfo.objects.filter(id=1)
# HeroInfo.objects.filter(id=1)
# HeroInfo.objects.filter(hbook_id=1)
# HeroInfo.objects.get(id=1)
# HeroInfo.objects.count(hbook_i=1)
# book = BookInfo.objects.get(id=2)
# book.heroinfo_set.all()
# hero = HeroInfo.objects.get(id=1)
# hero.hbook'
# hero = HeroInfo.objects.filter(hbook_id=1)
# hero.count()
# HeroInfo.objects.filter()
#
# try:
#     book = BookInfo.objects.get(id=18)
# except BookInfo.DoesNotExist:
#     pass
#
# BookInfo.objects.filter(btitle__contains="湖")
# BookInfo.objects.filter(btitle__contains='部')
# BookInfo.objects.filter(btitle__isnull=False)
# BookInfo.objects.filter(id__in=[2,4])
# BookInfo.objects.filter(id__gt=2)
# BookInfo.objects.exclude(id=3)
from datetime import datetime


class BooksAPIView(View):
    """
    查询所有图书、增加图书
    """
    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        books = BookInfo.objects.all()
        book_list = []
        for book in books:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            }
            book_list.append(book_dict)
        return JsonResponse(book_list, safe=False)


    def post(self,request):

        """新增一本书"""
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            bpub_date=datetime.strptime(book_dict.get('bpub_date'),'%Y-%m-%d').date()
        )
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            # 'image': book.image.url if book.image else ''
        }
        return JsonResponse(book_dict)

class BooksView(View):

    def get(self,request,pk):

        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
           return HttpResponse({'error'},status=404)
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            # 'image': book.image.url if book.image else ''
        }
        # 响应
        return JsonResponse(book_dict)

    def delete(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk).delete()
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)


        return HttpResponse(book)

    def put(self,request,pk):
        """修改指定书籍"""
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        json_dict = json.loads(json_str)
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'不存在'},status=404)


        #修改模型对象
        book.btitle = json_dict['btitle']
        book.bpub_date = json_dict['bpub_date']
        book.bread = json_dict.get('bread', book.bread)
        book.save()
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            # 'image': book.image.url if book.image else ''
        }
        return JsonResponse(book_dict)

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer