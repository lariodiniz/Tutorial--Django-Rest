#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('snippets.urls')),
]