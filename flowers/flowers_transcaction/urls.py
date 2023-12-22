# conding:utf-8
"""
#Time: 2023/12/19-15:12
#Author: tanchang
#File: urls.py
#Project: 鲜花库存管理系统
#Text: GoodGood学习！天天UpUp
"""


from django.urls import path
from . import views

app_name = 'flowers_transcaction'

urlpatterns = [
    path('inbound/<int:flower_id>', views.inbound_list, name='inbound'),
    path('outbound/<int:flower_id>', views.outbound_list, name='outbound'),
    path('outbound_list/<int:admin_id>',views.admin_out_list, name='admin_out_list'),
]