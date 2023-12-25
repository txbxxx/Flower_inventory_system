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
import  random


# 定义添加鲜花的Form表单
class FlowersForm(forms.ModelForm):
    class Meta:
        model = flower_data
        # fields = '__all__'：fields属性指定了表单应该包含模型中的哪些字段。'__all__'表示包含模型中的所有字段。这样，表单将包含模型中定义的所有字段。
        fields = ['flower_name','classi','num','price']
    def save(self, commit=True):
        instance = super(FlowersForm, self).save(commit=False)
        if not instance.pk:
            while True:
                new_flower_id = random.randint(10000, 99999)  # 生成一个随机的四位数作为class_id
                if not flower_data.objects.filter(flower_id=new_flower_id).exists():
                    instance.flower_id = new_flower_id
                    break
        if commit:
            instance.save()
        return instance


class FlowerClassForm(forms.ModelForm):
    class Meta:
        model = flower_class
        fields = ['class_name']

    def save(self, commit=True):
        instance = super(FlowerClassForm, self).save(commit=False)
        if not instance.pk:
            while True:
                new_class_id = random.randint(10000, 99999)  # 生成一个随机的四位数作为class_id
                if not flower_class.objects.filter(class_id=new_class_id).exists():
                    instance.class_id = new_class_id
                    break
        if commit:
            instance.save()
        return instance


class adminForm(forms.ModelForm):
    class Meta:
        model = admin_data
        fields = ['admin_name','telephone']
    def save(self, commit=True):
        instance = super(adminForm, self).save(commit=False)
        if not instance.pk:
            while True:
                new_admin_id = random.randint(10000, 99999)  # 生成一个随机的四位数作为class_id
                if not admin_data.objects.filter(admin_id=new_admin_id).exists():
                    instance.admin_id = new_admin_id
                    break
        if commit:
            instance.save()
        return instance

class SearchForm(forms.Form):
    query=forms.CharField()
