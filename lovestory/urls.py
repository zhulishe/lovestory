"""lovestory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from misslove.views import articles, comments, users

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),

    url(r'^$', articles.homepage, name='homepage'),
    url(r'^accounts/signup/$', 'misslove.views.users.sign_up', name='signup'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
	url(r'^accounts/info/(?P<user_id>\d+)/$', 'misslove.views.users.user_info', name="user_info"),
    url(r'^accounts/edit/(?P<user_id>\d+)/$', 'misslove.views.users.info_edit', name="info_edit"),
	url(r'^articles/new/$','misslove.views.articles.new_article', name="new_article"),
    url(r'^articles/catalog/(?P<article_type>\d+)/$', 'misslove.views.articles.article_catalog', name="article_catalog"),
	url(r'^articles/detail/(?P<article_id>\d+)/$', 'misslove.views.articles.article_detail', name="article_detail"),
    url(r'^articles/delete/(?P<article_id>\d+)/$', 'misslove.views.articles.article_delete', name="article_delete"),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




