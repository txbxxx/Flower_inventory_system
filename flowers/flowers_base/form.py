# conding:utf-8
"""
#Time: 2023/12/19-15:59
#Author: tanchang
#File: form.py
#Project: 鲜花库存管理系统
#Text: GoodGood学习！天天UpUp
"""

from django import forms
from .models import flower_data, flower_class, admin_data


# 定义添加鲜花的Form表单
class FlowersForm(forms.ModelForm):
    class Meta:
        model = flower_data
        # fields = '__all__'：fields属性指定了表单应该包含模型中的哪些字段。'__all__'表示包含模型中的所有字段。这样，表单将包含模型中定义的所有字段。
        fields = '__all__'


class FlowerClassForm(forms.ModelForm):
    class Meta:
        model = flower_class
        fields = '__all__'


class adminForm(forms.ModelForm):
    class Meta:
        model = admin_data
        fields = '__all__'
