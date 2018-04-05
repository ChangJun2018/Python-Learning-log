# -*- coding: UTF-8 -*-
"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

#可在应用程序中请求的网页
urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
    #显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #特定主题的详细页面
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
]
app_name = 'learning_logs'