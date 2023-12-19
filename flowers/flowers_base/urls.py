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
    path('', views.index, name="index"),
    path('flower_data/',views.flower_data, name="flower_data")
]

