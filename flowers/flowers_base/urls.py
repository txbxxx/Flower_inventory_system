# coding=utf-8
"""
================================================================

author: Tan Chang 
file: urls.py
date:2023/12/19

================================================================
"""

from django.urls import path
from . import views

app_name = "flowers_base"

urlpatterns = [
    path('', views.index, name="index"),  # 主页路由
    path('flower_data/', views.flowers_data, name="flower_data"),  # flower_data界面的路由
    path('flower_class/', views.flowerClass, name="flower_class"),  # flower_class界面路由
    path('admin_data/', views.adminData, name="admin_data"), # 管理员界面路由
    path('add_flower', views.add_flower, name="add_flower"),  # 添加Flower的form表单路由
    path('add_flowerclass', views.add_flowerclass, name="add_flowerclass"),  # 添加Flower class的form表单路由
    path('add_admin', views.add_admin, name="add_admin"),  # 添加Flower class的form表单路由
]
