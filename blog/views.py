# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404


from django.contrib.syndication.views import Feed  

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  


# Create your views here.
def home(request):
    #return HttpResponse("Hello World, Django")
    """
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
    """
    posts = Article.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, my_args):
    # return HttpResponse("You are looking at my_args %s." % my_args)
    """
    post = Article.objects.all()[int(my_args)]
    str = ("title=%s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
    """
    try:
        post = Article.objects.get(id=str(my_args))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html', {'post_list': post_list,'error': False})

def about_me(request):
    return render(request, 'aboutme.html')

def search_tag(request, tag):
    try: 
        post_list = Article.objects.filter(category__iexact = tag) # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})
    return redirect('/')

class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content
