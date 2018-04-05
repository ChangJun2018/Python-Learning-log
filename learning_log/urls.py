# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.urls import path, include

#定义变量，包含项目中的应用程序的url
urlpatterns = [
    #定义了管理网站请求的所有url
    path('admin/', admin.site.urls),
    path(r'^users/', include('users.urls', namespace='users')),
    path('', include('learning_logs.urls', namespace='learning_logs')),
]