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
    path('edit_flower/<int:flower_id>/', views.edit_flower, name="edit_flower"), # 编辑花的信息的路由
    path('delete_flower/<int:flower_id>/', views.delete_flower, name="delete_flower"), # 删除花的信息
    path('class_flower/<int:class_id>/', views.class_flower, name="class_flower"), #花的类别
    path('search/', views.search_flower, name="search_flower"), #查询功能
    path('delete_class/<int:class_id>/', views.delete_class, name="delete_class"), #删除花的类别
    path('edit_class/<int:class_id>/', views.edit_class, name="edit_class"),  #修改花的类别
    path('edit_admin/<int:admin_id>/', views.edit_admin, name="edit_admin"),
    path('delete_admin/<int:admin_id>/', views.delete_admin, name="delete_admin"),
]
