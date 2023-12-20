# conding:utf-8
"""
---------------------------------------------
#Time: 2023/12/19-21:10
#Author: tanchang
#File: form.py
#Project: 鲜花库存管理系统
#Text: GoodGood学习！天天UpUp
---------------------------------------------
"""

from django import forms
from .models import inbound, outbound


class InBoundForm(forms.ModelForm):
    class Meta:
        model = inbound
        fields = '__all__'


class OutBoundForm(forms.ModelForm):
    class Meta:
        model = outbound
        fields = '__all__'
