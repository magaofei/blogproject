from django.conf.urls import url
from . import views


app_name = 'blog'
# 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间
urlpatterns = [
    url(r'^$', views.index, name='index'),  #name，这个参数的值将作为处理函数 index 的别名
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
