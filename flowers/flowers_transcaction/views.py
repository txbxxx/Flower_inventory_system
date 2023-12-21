from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from .form import InBoundForm, OutBoundForm
from flowers_base.models import flower_data


# Create your views here.

# （可用了）此处有问题，在点击入库表单无反应
#入库视图操作
def inbound(request, flower_id):
    # 获取flower对象，依靠传入的flower_id
    flower = flower_data.objects.get(flower_id=flower_id)
    init_data = {'flowers': flower.flower_name}     #初始化数据，点击哪个花就默认显示哪个花
    if request.method != 'POST': #判断如果不是POST提交请求，则是GET获取请求
        form = InBoundForm(initial=init_data)  # 就创建一个Form表单并给与初始化值
        form.fields['flowers'].queryset = flower_data.objects.filter(flower_id=flower_id) #限制只允许选择当前花
    else:
        form = InBoundForm(data=request.POST) #提交请求，提交写入的数据
        if form.is_valid():
            num = form.cleaned_data['inbound_num']  # 获取表单中的数据，并进行后续的处理
            flower.num += num  #将花本身的个数加上入库的个数
            flower.save()   #保存花的数据
            form.save()     #保存表单的数据
            return HttpResponseRedirect(reverse('flowers_base:flower_data'))
    context = {'form': form, "flower": flower}
    return render(request, 'flowers_transcaction/inbound.html', context)


# 出库视图操作操作同入库视图
def outbound(request, flower_id):
    flower = flower_data.objects.get(flower_id=flower_id)
    init_data = {'flowers': flower.flower_name}
    if request.method != 'POST':
        form = OutBoundForm(initial=init_data)
        form.fields['flowers'].queryset = flower_data.objects.filter(flower_id=flower_id)
    else:
        form = OutBoundForm(initial=init_data,data=request.POST)
        if form.is_valid():
            num = form.cleaned_data['outbound_num']  # 获取表单中的数据，并进行后续的处理
            flower.num -= num
            form.save()
            flower.save()
            return HttpResponseRedirect(reverse('flowers_base:flower_data'))
    context = {'form': form, "flower": flower}
    return render(request, 'flowers_transcaction/outbound.html', context)
