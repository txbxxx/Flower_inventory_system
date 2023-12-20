from django.shortcuts import render, redirect
from .models import flower_data, flower_class, admin_data
from .form import FlowersForm, FlowerClassForm, adminForm


# Create your views here.

# 主页视图urls.py文件中指向
def index(request):
    return render(request, 'flowers_base/index.html')


# flower_data的视图方法
def flowers_data(request):
    flowers = flower_data.objects.order_by('flower_id')  # 获取数据库中的数据，并且按照flower_id来排序
    context = {'flowers': flowers}  # 在html文件中将flowers直接映射为flowers，在render中调用了
    return render(request, 'flowers_base/flowers_data.html', context)


def flowerClass(request):
    class_data = flower_class.objects.order_by('class_id')
    context = {'class_data': class_data}
    return render(request, 'flowers_base/class_data.html', context)


def adminData(request):
    admindata = admin_data.objects.order_by('admin_id')
    context = {'admin_data': admindata}
    return render(request, 'flowers_base/admin_data.html', context)


# 向数据库中添加flower的方法
def add_flower(request):
    if request.method != 'POST':  # 如果不是POST请求就创建一个空表单，请求一般是get请求
        form = FlowersForm()
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

#修改
def edit_flower(request, flower_id):
    flower = flower_data.objects.get(flower_id=flower_id)
    clas = flower.classi
    if request.method != 'POST':
        form = FlowersForm(instance=flower)
    else:
        form = FlowersForm(instance=flower, data=request.POST)
        if form.is_valid():
            form.save()
            redirect('flowers_base:flower_class')
    context = {'form': form, "clas": clas, "flower": flower}
    return render(request, 'flowers_base/edit_flower.html', context)


# 删除鲜花视图
def delete_flower(request, flower_id):
    flower_id = flower_data.objects.get(flower_id=flower_id)
    flower_id.delete()
    return redirect('flowers_base:flower_data')
    # return render(request, 'flowers_base/delete_flowers.html')


def class_flower(request, class_id):
    print(class_id)
    flower = flower_data.objects.filter(classi=class_id)
    context = {'flower': flower}
    return render(request, 'flowers_base/class_flower_list.html', context)
