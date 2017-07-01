from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # - 表示逆序
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(
        post.body,
        # 注意这里我们给 markdown 渲染函数传递了额外的参数 extensions，它是对 Markdown 语法的拓展，这里我们使用了三个拓展，分别是 extra、codehilite、toc。extra 本身包含很多拓展，而 codehilite 是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，而 toc 则允许我们自动生成目录（在以后会介绍）。
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
    ])

    return render(request, 'blog/detail.html', context={'post': post})
