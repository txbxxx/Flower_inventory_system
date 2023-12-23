from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import flower_data, flower_class, admin_data
from .form import FlowersForm, FlowerClassForm, adminForm, SearchForm
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid

# Create your views here.

# 主页视图urls.py文件中指向
def index(request):
    return render(request, 'flowers_base/index.html')


# flower_data的视图方法
def flowers_data(request):
    flowers = flower_data.objects.order_by('flower_id')  # 获取数据库中的数据，并且按照flower_id来排序
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(flowers, 10)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
    }  # 在html文件中将flowers直接映射为flowers，在render中调用了
    return render(request, 'flowers_base/flowers_data.html', context)


#flower类别视图
def flowerClass(request):
    class_data = flower_class.objects.order_by('class_id')
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(class_data, 10)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
    }
    return render(request, 'flowers_base/class_data.html', context)

#管理员用户视图
def adminData(request):
    admindata = admin_data.objects.order_by('admin_id')
    page_number = request.GET.get('page', 1)  ## 页码
    paginator = Paginator(admindata, 10)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
    }
    return render(request, 'flowers_base/admin_data.html', context)


# 向数据库中添加flower的方法
def add_flower(request):
    if request.method != 'POST':  # 如果不是POST请求就创建一个空表单，请求一般是get请求
        form = FlowersForm(initial={'flower_id': str(uuid.uuid4())})
        print(form)
    else:
        form = FlowersForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('flowers_base:flower_data')
    context = {'form': form}
    return render(request, 'flowers_base/add_flower.html', context)


# 添加鲜花类视图
def add_flowerclass(request):
    if request.method != 'POST':  # 如果不是POST请求就创建一个空表单，请求一般是get请求
        form = FlowerClassForm()
    else:
        form = FlowerClassForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('flowers_base:flower_class')
    context = {'form': form}
    return render(request, 'flowers_base/add_flowerclass.html', context)


## 添加管理员视图
def add_admin(request):
    if request.method != 'POST':
        form = adminForm()
    else:
        form = adminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('flowers_base:admin_data')
    context = {'form': form}
    return render(request, 'flowers_base/add_admin.html', context)

#修改花的信息
def edit_flower(request, flower_id):
    flower = flower_data.objects.get(flower_id=flower_id)
    clas = flower.classi
    if request.method != 'POST':
        form = FlowersForm(instance=flower)
    else:
        fl = int(request.POST.get('flower_id'))
        form = FlowersForm(instance=flower, data=request.POST)
        if fl == flower_id:
            if form.is_valid():
                #检测用户是否修改了flower_name
                if 'flower_name' not in request.POST:
                    form.save()
                    return redirect('flowers_base:flower_data',)
        else:
            messages.error(request, "flower_id不能被修改")
    context = {'form': form, "clas": clas, "flower": flower}
    return render(request, 'flowers_base/edit_flower.html', context)



#修改花的类别信息
def edit_class(request, class_id):
    class_i = flower_class.objects.get(class_id=class_id)
    if request.method != 'POST':
        form = FlowerClassForm(instance=class_i)
    else:
        ci = int(request.POST.get('class_id'))
        form = FlowerClassForm(instance=class_i, data=request.POST)
        if ci == class_id: #检查是否修改了class_id
            if form.is_valid():
                form.save()
                return redirect('flowers_base:flower_class')
        else: ##如果修改了就报错
            messages.error(request, "class_id不能被修改")
    context = {'form':form, "class_i": class_i}
    return render(request, 'flowers_base/edit_class.html', context)


#修改管理员信息
def edit_admin(request, admin_id):
    admin = admin_data.objects.get(admin_id=admin_id)
    if request.method != 'POST':
        form = adminForm(instance=admin)
    else:
        admini = int(request.POST.get("admin_id"))
        form = adminForm(instance=admin, data=request.POST)
        if admin_id != admini:  # 检查是否修改了admin_id
            messages.error(request, "admin_id不能被修改")
        else:
            form.save()
            return redirect('flowers_base:admin_data')
    context = {'form':form, "admin": admin}
    return render(request, 'flowers_base/edit_admin.html', context)

# 删除鲜花视图
def delete_flower(request, flower_id):
    flower_id = flower_data.objects.get(flower_id=flower_id)
    flower_id.delete()
    return redirect('flowers_base:flower_data')
    # return render(request, 'flowers_base/delete_flowers.html')

#删除花类别视图
def delete_class(request, class_id):
    class_id = flower_class.objects.get(class_id=class_id)
    class_id.delete()
    return redirect('flowers_base:flower_class')

#删除管理员视图
def delete_admin(request, admin_id):
    admin = admin_data.objects.get(admin_id=admin_id)
    admin.delete()
    return redirect('flowers_base:admin_data',)


#在flower_class界面中点击花的类别名就可以查看花的分类
def class_flower(request, class_id):
    flower = flower_data.objects.filter(classi=class_id)
    class_name = None
    if flower.exists():
        class_name = flower[0].classi.class_name
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(flower, 10)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
        'class_id':class_id
    }
    return render(request, 'flowers_base/class_flower_list.html', context)


#搜索视图用法
def search_flower(request):
    #获取值，这个值是input输入的内容，其中select是input输入框的name
    form = request.GET.get("select",None)
    pattern = "^[0-9]+$"
    #Q是表示可以使用or and这些来搜索
    if form:
        if re.match(pattern, form):
            modle = flower_data.objects.filter(
                Q(flower_id=form)).order_by('-flower_id').all()
        else:
            modle = flower_data.objects.filter(
                Q(flower_name__icontains=form) | Q(classi__class_name__icontains=form)).order_by('-flower_id').all()
    else:
        modle = flower_data.objects.all().order_by('-flower_id')
    # search = flower_data.objects.filter(Q(flower_name__icontains=form) | Q(flower_id__icontains=form) |Q(classi__class_name__icontains=form))
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(modle, 10)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
        'key': form
    }
    return render(request,'flowers_base/search.html',context)

def search_surplus(request):
    form = request.GET.get('search_surplus')
    print(form)
    pattern = "^[0-9]+$"
    modle = flower_data.objects.all()
    if form and re.match(pattern, form):
            modle = flower_data.objects.filter(num__lt=form)
    page_number = request.GET.get('page') ## 页码
    paginator = Paginator(modle, 10)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
    }
    return render(request,'flowers_base/search_surplus.html',context)



