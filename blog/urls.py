from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  #name，这个参数的值将作为处理函数 index 的别名
]
