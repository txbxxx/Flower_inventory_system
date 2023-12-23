from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect, HttpResponse
from .form import InBoundForm, OutBoundForm
from .models import inbound,outbound
from flowers_base.models import flower_data
from django.contrib import messages

# Create your views here.

# （可用了）此处有问题，在点击入库表单无反应
#入库视图操作
def inbound_list(request, flower_id):
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
            form.save_inbound()     #保存表单的数据
            return HttpResponseRedirect(reverse('flowers_base:flower_data'))
    context = {'form': form, "flower": flower}
    return render(request, 'flowers_transcaction/inbound.html', context)


# 出库视图操作操作同入库视图
def outbound_list(request, flower_id):
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
            if flower.num < 0:
                messages.error(request, "库存数量不足")
            else:
                form.save()
                flower.save()
                return HttpResponseRedirect(reverse('flowers_base:flower_data'))
    context = {'form': form, "flower": flower}
    return render(request, 'flowers_transcaction/outbound.html', context)



#对应管理员的出库表清单
def admin_bond_list(request, admin_id):
    out = outbound.objects.filter(admin_id=admin_id)
    ino = inbound.objects.filter(admin_id=admin_id)
    admin_name = None   #首先将管理员的名字设置为None调用到html中使用if判断
    ##如果inbount内有数据就执行
    if ino.exists():
        admin_name = ino[0].admin.admin_name  # 获取管理员的名字
    ##如果outbount内有数据就执行
    if out.exists():
        admin_name = out[0].admin.admin_name  # 获取管理员的名字
    context = {'out': out, 'admin_name': admin_name,'ino':ino}
    return render(request, 'flowers_transcaction/admin_oprate_list.html', context)


#输出总的出库表
def bond_list(request):
    out = outbound.objects.order_by('outbound_date')
    ino = inbound.objects.order_by('inbound_date')
    # page_number = request.GET.get('page', 1) ## 页码
    # paginator = Paginator(out, 10)
    # page_obj = paginator.get_page(page_number)
    context = {
        # 'page_obj': page_obj,
        # 'paginator': paginator,
        # 'current_page': page_number,
        'out':out,
        'ino':ino,
    }
    return render(request, 'flowers_transcaction/bound_all_list.html', context)





#删除出库信息后，花的数据返回
def delete_inbound(request, inbound_id):
    inbound_data = inbound.objects.get(inbound_id=inbound_id)
    #获取flower对象依靠inbound_data的外键】】‘
    flower = flower_data.objects.get(flower_id=inbound_data.flowers.flower_id)
    #如果入库花的数量是大于小于或等于花现在的数量，那么就表示为正常
    if inbound_data.flowers.num >= inbound_data.inbound_num:
        flower.num -= inbound_data.inbound_num
        inbound_data.delete()
        flower.save()
        return redirect('flowers_transcaction:admin_bond_list',inbound_data.admin.admin_id  )
    else:
        messages.error(request, "不能删除！！，因为库存不足，请检查出库入库表单！！")


#删除出库信息后，数据返回
def delete_outbound(request, outbound_id):
    # 获取flower对象，依靠传入的flower_id
    outbound_data = outbound.objects.get(outbound_id=outbound_id)
    flower = flower_data.objects.get(flower_id=outbound_data.flowers.flower_id)
    flower.num += outbound_data.outbound_num
    outbound_data.delete()
    flower.save()
    return redirect('flowers_transcaction:admin_bond_list',outbound_data.admin.admin_id )