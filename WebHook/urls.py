# -*- coding: utf-8 -*-  
from django.conf.urls import patterns, include, url
from WebHook.views import query_form
from WebHook.views import insert
from WebHook.views import test
from WebHook.views import check


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebHook.views.home', name='home'),
    # url(r'^WebHook/', include('WebHook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # url('^$',)
    url(r'^$',query_form),
    url(r'^insert/$', insert),
    url(r'^check/$',check),
)
