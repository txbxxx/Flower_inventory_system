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
    path('inbound/<int:flower_id>', views.inbound_list, name='inbound'), #入库表视图
    path('outbound/<int:flower_id>', views.outbound_list, name='outbound'), #出库表视图
    path('bound_list/<int:admin_id>',views.admin_bond_list, name='admin_bond_list'), #管理员操作出库入库视图
    path('delete_inbound_data/<int:inbound_id>',views.delete_inbound, name='delete_inbound'), #删除入库视图
    path('delete_outbound_data/<int:outbound_id>',views.delete_outbound, name='delete_outbound'),
    path('bound_list/',views.bond_list, name='bound_list'), #整体出库入库表视图
    # path('in_bound_list/',views.in_bond_list, name='in_bound_list'),
]