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
    path('bound_list/<int:admin_id>',views.admin_bond_list, name='admin_bond_list'),
    path('delete_inbound_data/<int:inbound_id>',views.delete_inbound, name='delete_inbound'),
    path('delete_outbound_data/<int:outbound_id>',views.delete_outbound, name='delete_outbound'),
    path('bound_list/',views.bond_list, name='bound_list'),
    # path('in_bound_list/',views.in_bond_list, name='in_bound_list'),
]