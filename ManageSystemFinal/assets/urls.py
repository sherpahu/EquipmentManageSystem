#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path
from assets import views

app_name = 'assets'

urlpatterns = [
	path('index/', views.index, name='index'),
	path('login/', views.login,name="login"),
	path('add/', views.add, name="add"),
	path('index/add/', views.add, name="add"),
	path('', views.index, name="admin"),
	path('del/(?P<asset_id>[0-9]+)/$', views.del_equipment, name="del_equipment"),
]

