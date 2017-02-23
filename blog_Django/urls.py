# -*- coding:utf-8 -*-
"""blog_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
from blog.views import RSSFeed

urlpatterns = [
    url(r'^$', blog_views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    # url(r'^(?P<my_args>\d+)/$', blog_views.detail, name='detail'),        
    url(r'^article/(?P<my_args>\d+)/$', blog_views.detail, name='detail'),    
    url(r'^test/$', blog_views.test, name='test'),
    url(r'^archives/$', blog_views.archives, name='archives'),
    url(r'^aboutme/$', blog_views.about_me, name='aboutme'),
    url(r'^tag(?P<tag>\w+)/$', blog_views.search_tag, name='search_tag'),
    url(r'^search/$', blog_views.blog_search, name='search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"), #新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url 
    ]
