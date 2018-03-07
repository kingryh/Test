'''
from django.conf.urls import url,include
from django.contrib import admin
'''
from django.conf.urls import url

from . import views

"""
绑定URL与视图函数
首先Django需要知道当用户访问不同的网址时，应该如何处理这些不同的网址（即所说的路由）
Django的做法是把不同的网址对应的处理函数写在一个urls.py文件里，当用户访问某个网址时，
Django就去会这个文件里找，如果找到这个网址，就会调用和它绑定在一起的处理函数(视图函数)
设计文章详情页的URL
"""

#告诉Django这个urls.py模块是属于blog应用，这种技术叫做视图函数命名空间。
app_name ='blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #这条正则表达式的含义是:以post/开头，后跟一个至少一位数的数字，并且以/符号结尾，如post/1/、
    #post/255/等都是符合规则的,[0-9]+表示一位或多位数。此外(?P<pk>[0-9]+)表示命名捕获组,
    #其作用是从用户访问的URL里把过好内匹配的字符串捕获并作为关键字参数传给其对应的试图函数detail
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
]
'''
配置项目URL

'''