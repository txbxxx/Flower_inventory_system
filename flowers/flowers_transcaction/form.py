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
import random
from datetime import datetime

class InBoundForm(forms.ModelForm):
    class Meta:
        model = inbound
        fields = ['inbound_num','admin','flowers']
    def save_inbound(self, commit=True):
        instance = super(InBoundForm, self).save(commit=False)
        ##使用时间来完成
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y%m%d%H%M%S")
        instance.inbound_id = formatted_time
        # while True: #判断如果随机生成的数存就继续生成
        #     # new_inbound_id = random.randint(10000, 99999)  # 生成一个随机的四位数作为class_id(遗弃)
        #     if not inbound.objects.filter(inbound_id=new_inbound_id).exists():
        #         instance.inbound_id = new_inbound_id
        #         break
        if commit:
            instance.save()
        return instance


class OutBoundForm(forms.ModelForm):
    class Meta:
        model = outbound
        fields = ['outbound_num','admin','flowers']

    def save(self, commit=True):
        instance = super(OutBoundForm, self).save(commit=False)
        while True:
            new_outbound_id = random.randint(10000, 99999)  # 生成一个随机的四位数作为class_id
            if not outbound.objects.filter(outbound_id=new_outbound_id).exists():
                instance.outbound_id = new_outbound_id
                break
        if commit:
            instance.save()
        return instance
