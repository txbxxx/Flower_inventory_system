### 一、选题介绍

本项目是一个依据课程设计选题来做的

#### 1.1 课程设计的目的和要求

**鲜花库存管理系统的要求有：**

1. 实现鲜花信息（鲜花编号、名称、类别号、单价、库存数），管理员信息（工号、姓名、联系电话）
2. 鲜花类别信息（类别号、类别名称）的插入、删除、修改、浏览和查询管理；
3. 实现鲜花的出库管理（出库单号、鲜花编号、出库数量、出库时间、管理员工号）；实
4. 现鲜花的入库管理（入库单号、鲜花编号、入库数量、入库时间、管理员工号）；
5. **建立数据库相关表之间的参照完整性约束；**创建视图，按类别查询不同鲜花的编号、名称、总数和库存量；
6. 创建存储过程，查询库存数少于指定数目的在库鲜花信息，以便进货；
7. 创建触发器，其功能是：当删除某条鲜花信息记录时，该鲜花的出库信息和出库信息也一并删除

#### 1.2问题描述

问题描述：

设计一个鲜花库存管理系统，该系统需要实现以下功能：

1. 鲜花信息管理：包括鲜花编号、名称、类别号、单价、库存数的插入、删除、修改、浏览和查询管理。

2. 管理员信息管理：包括工号、姓名、联系电话的插入、删除、修改、浏览和查询管理。

3. 鲜花类别信息管理：包括类别号、类别名称的插入、删除、修改、浏览和查询管理。

4. 鲜花出库管理：包括出库单号、鲜花编号、出库数量、出库时间、管理员工号的插入、删除、修改、浏览和查询管理。

5. 鲜花入库管理：包括入库单号、鲜花编号、入库数量、入库时间、管理员工号的插入、删除、修改、浏览和查询管理。

6. 建立数据库相关表之间的参照完整性约束。

7. 创建视图，按类别查询不同鲜花的编号、名称、总数和库存量。

8. 创建存储过程，查询库存数少于指定数目的在库鲜花信息，以便进货。

9. 创建触发器，其功能是：当删除某条鲜花信息记录时，该鲜花的出库信息和出库信息也一并删除。





#### 二、系统分析与设计

#### 2.1系统分析

(1)数据需求：需要创建5个数据表

1.首先为鲜花的数据表：字段有鲜花名、ID、类别号、库存数量、单价，鲜花名需要定义为char类型，其余均可定义为int，且鲜花名字和ID必须要唯一，类别号外键指向类别表；

2.鲜花类别表：字段有类别号和类别名，两个都是唯一字段

3.管理员表：字段有管理员名字、管理员ID、联系电话，管理员的ID为唯一

4.出库/入库数据表：记录管理员操作的时候的出库入库的记录，字段有出库单号，出库数量， 出库时间，操作员名，出库的鲜花，出库单号为唯一，操作员名字和出库鲜花分比外键指向管理员表和鲜花表

(2)功能需求：

1.前端基本功能显示各个数据表内的数据

2.添加\删除\修改鲜花、添加\删除\修改管理员、添加\删除\修改鲜花类别的操作

3.对鲜花进行出库入库的操作，并且删除鲜花相应的入库和出库操作也会删除

4.添加管理员，管理员可以查看自己的入库出库记录

5.可以搜索鲜花名、鲜花ID、鲜花库存、鲜花单价、管理员名、管理ID、管理员联系方式、鲜花类别号和类别名等操作

6.在鲜花表界面中，可以搜索剩余数量大于小于搜索数的

7.各类ID可以通过随机生成和时间戳来生成不一样的ID

8.删除了类别类别所属的鲜花也要一并删除，删除了出库入库记录，鲜花的库存数量需要回退，并且当鲜花数量不足入库数量时需要判断

(3)数据流图

![image-20231224152141452](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224152141452.png)

#### 2.2数据库设计





### 三、系统实现与测试

#### 3.1系统实现

​	本项目使用`Django`+`bootstrap`来作为前端后端，我创建了一个`Python`的虚拟环境将`Django`安装在虚拟环境内，在创建`Django`项目名为`flowers_manager_systemctl`作为本次课设的主体文件，随后又创建了两个应用程序分别名为`flower_base`和`flower_tanscaction` ，前者是作为鲜花库存系统的基础功能增删改查和搜索，后者则是出库入库系统；

##### 1.flower_base

1)创建数据表，`Django`中的数据表都是依照模型来创建，在应用程序中创建鲜花、类别、管理员的模型文件在**应用程序**下的`modle.py`

```python
from django.db import models


# Create your models here.

# 鲜花类别模型
class flower_class(models.Model):
    # 定义类别号、类别名称
    class_id = models.IntegerField(primary_key=True, unique=True)
    class_name = models.CharField(max_length=30, unique=True)
    #显示类别名字
    def __str__(self):
        return self.class_name


# 定义鲜花模型
class flower_data(models.Model):
    # 定义编号、名称、类别号、单价、库存数
    flower_id = models.IntegerField(primary_key=True, unique=True)
    flower_name = models.CharField(max_length=20, unique=True)
    # 设置外键指向flower_class，如果flower_class删除关于这个类别的所有鲜花也都删除
    classi = models.ForeignKey(flower_class,to_field="class_id", on_delete=models.CASCADE)
    price = models.DecimalField(null=True, max_digits=15, decimal_places=2)
    num = models.IntegerField()

    #显示flower的名字
    def __str__(self):
        return self.flower_name


# 管理员模型
class admin_data(models.Model):
    # 定义管理员工号、姓名、电话
    admin_id = models.IntegerField(primary_key=True, unique=True)
    admin_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30, null=True)
    #显示管理员的名字
    def __str__(self):
        return self.admin_name
```

2)如果需要通过form表单来创建或者修改数据的话，可以直接调用Django提供的Form表单功能，这样就可以省很多为Form表单传送数据的问题，如果要创建`Django`-`Form`表单的话，我这里为了便于管理就创建了一个单独的`form.py`文件

每个Form表单都是基于一个模型创建的，自动读取模型内的字段来生成，这里我创建了一个自动生成ID字段的方法并且通过`if not instance.pk:`来判断是否被保存过，如果没有那就创建

```python
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

```

3)需要在前端显示创建好的数据表内的数据就需要通过修改Django的`url`和`view`来实现，我这里为了便于管理，每个应用程序都有自己的`url.py`文件



​		`	url.py`文件，每条数据后都有备注其功能，`url`只是可以让前端调用的路由，不是实现数据拉取，当前端调用了这个路由，路由就会调用它相对应的视图`views`

```python
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
    path('', views.index, name="index"),  # 主页路由
    path('flower_data/', views.flowers_data, name="flower_data"),  # flower_data界面的路由
    path('flower_class/', views.flowerClass, name="flower_class"),  # flower_class界面路由
    path('admin_data/', views.adminData, name="admin_data"), # 管理员界面路由
    path('add_flower', views.add_flower, name="add_flower"),  # 添加Flower的form表单路由
    path('add_flowerclass', views.add_flowerclass, name="add_flowerclass"),  # 添加Flower class的form表单路由
    path('add_admin', views.add_admin, name="add_admin"),  # 添加Flower class的form表单路由
    path('edit_flower/<int:flower_id>/', views.edit_flower, name="edit_flower"), # 编辑花的信息的路由
    path('delete_flower/<int:flower_id>/', views.delete_flower, name="delete_flower"), # 删除花的信息
    path('class_flower/<int:class_id>/', views.class_flower, name="class_flower"), #花的类别
    path('search/', views.search_flower, name="search_flower"), #查询功能
    path('delete_class/<int:class_id>/', views.delete_class, name="delete_class"), #删除花的类别
    path('edit_class/<int:class_id>/', views.edit_class, name="edit_class"),  #修改花的类别
    path('edit_admin/<int:admin_id>/', views.edit_admin, name="edit_admin"),    #修改管理员的信息
    path('delete_admin/<int:admin_id>/', views.delete_admin, name="delete_admin"),  #删除管理员信息
    path('search_surplus/', views.search_surplus, name="search_surplus"), #查询剩余数量
]
```

​		`		views.py`文件没个视图函数（方法）都有一个固定的作用，是实现功能的主要，完成后会通过render来把数据传入相应的前端文件，以下是整体文件

```python
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import flower_data, flower_class, admin_data
from .form import FlowersForm, FlowerClassForm, adminForm, SearchForm
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid
from flowers_transcaction.models import inbound,outbound

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
        # fl = int(request.POST.get('flower_id'))
        form = FlowersForm(instance=flower, data=request.POST)
        # if fl == flower_id:
        if form.is_valid():
            #检测用户是否修改了flower_name
            # if 'flower_id' in request.POST:
            form.save()
            return redirect('flowers_base:flower_data',)
        # else:
        #     messages.error(request, "flower_id不能被修改")
    context = {'form': form, "clas": clas, "flower": flower}
    return render(request, 'flowers_base/edit_flower.html', context)



#修改花的类别信息
def edit_class(request, class_id):
    class_i = flower_class.objects.get(class_id=class_id)
    if request.method != 'POST':
        form = FlowerClassForm(instance=class_i)
    else:
        # ci = int(request.POST.get('class_id'))
        form = FlowerClassForm(instance=class_i, data=request.POST)
        # if ci == class_id: #检查是否修改了class_id
        if form.is_valid():
            form.save()
            return redirect('flowers_base:flower_class')
        # else: ##如果修改了就报错
        #     messages.error(request, "class_id不能被修改")
    context = {'form':form, "class_i": class_i}
    return render(request, 'flowers_base/edit_class.html', context)


#修改管理员信息
def edit_admin(request, admin_id):
    admin = admin_data.objects.get(admin_id=admin_id)
    if request.method != 'POST':
        form = adminForm(instance=admin)
    else:
        # admini = int(request.POST.get("admin_id"))
        form = adminForm(instance=admin, data=request.POST)
        # if admin_id != admini:  # 检查是否修改了admin_id
        #     messages.error(request, "admin_id不能被修改")
        # else:
        if form.is_valid():
            form.save()
            return redirect('flowers_base:admin_data')
    context = {'form':form, "admin": admin}
    return render(request, 'flowers_base/edit_admin.html', context)

# 删除鲜花视图
def delete_flower(request, flower_id):
    flower_id = flower_data.objects.get(flower_id=flower_id)
    flower_id.delete()
    return redirect('flowers_base:flower_data')

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


#搜索视图用法（本来想做全部搜索的，也就是admin，class也加进去,先把视图搜索，后面数据导入到HTML构思半天没构思好，先放着）
def search_flower(request):
    #获取值，这个值是input输入的内容，其中select是input输入框的name
    form = request.GET.get("select",None)
    pattern = "^[0-9]+$"
    #Q是表示可以使用or and这些来搜索
    if form:
        if re.match(pattern, form):
            modle1 = flower_data.objects.filter(
                Q(flower_id=form) | Q(classi=form) | Q(price=form) | Q(num=form))
            modle2 = admin_data.objects.filter(
                Q(admin_id=form)
            )
            modle3 = flower_class.objects.filter(
                Q(class_id=form)
            )
            modle = list(modle1)+list(modle2)+list(modle3)
        else:
            modle1 = flower_data.objects.filter(
                Q(flower_name__icontains=form) | Q(classi__class_name__icontains=form)).order_by('-flower_id').all()
            modle2 = admin_data.objects.filter(
                Q(admin_name__icontains=form)  | Q(telephone__icontains=form)
            )
            modle3 = flower_class.objects.filter(
                Q(class_name__icontains=form)
            )
            modle = list(modle1) + list(modle2)+list(modle3)
    else:
        modle = flower_data.objects.all().order_by('-flower_id')
    # search = flower_data.objects.filter(Q(flower_name__icontains=form) | Q(flower_id__icontains=form) |Q(classi__class_name__icontains=form))
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(modle, 10)
    page_obj = paginator.get_page(page_number)
    # if isinstance(page_obj.object_list[0], flower_data):
    #     n = 1;
    # elif isinstance(page_obj.object_list[0],flower_class):
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
        'key': form
    }
    return render(request,'flowers_base/search.html',context)


##这个是查询是否小于这个库存数
def search_surplus(request):
    form = request.GET.get('search_surplus')
    pattern = "^[0-9]+$"
    modle = flower_data.objects.all()
    if form and re.match(pattern, form):
            modle = flower_data.objects.filter(num__lt=form)
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(modle, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
    }
    return render(request,'flowers_base/search_surplus.html',context)




```

3.1.1获取数据库数据并显示

以下是实现读取鲜花数据的视图，启动使用了`django`的`objects`来获取`flower_data数据表`内的数据并以`flower_id`来排序，使用了分页器将数据每10条一页，随后将分页器和分页器的数据传入到指定的`html`文件，类别和管理员的视图都是这样

```Python
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
```

3.1.2修改

​	从模型中使用`object.get`来获取传入的`flower_id`,`flower_id`是在`html`文件中传入的，只要调用的了它的`url`就需要传入参数，也就是说，这个无论在项目中的那个`html`文件都可以调用它来处理修改花的数据，并且判断获是不是一个POST数据如果不是就生成一个表单并填写它之前就信息，如果是就将他修改的数据和之前的数据一起提交，删除其余的代码也和这个类似

```python
#修改花的信息
def edit_flower(request, flower_id):
    flower = flower_data.objects.get(flower_id=flower_id)
    clas = flower.classi
    if request.method != 'POST':
        form = FlowersForm(instance=flower)
    else:
        form = FlowersForm(instance=flower, data=request.POST)
            if form.is_valid():
                #检测用户是否修改了flower_name
                form.save()
                return redirect('flowers_base:flower_data',)
        else:
            messages.error(request, "flower_id不能被修改")
    context = {'form': form, "clas": clas, "flower": flower}
    return render(request, 'flowers_base/edit_flower.html', context)
```

3.1.3删除

​	这里使用了.`delete()`来删除，和修改数据开始同样的办法，也是传入ID然后删除鲜花，其余也是类似

```python
def delete_flower(request, flower_id):
    flower_id = flower_data.objects.get(flower_id=flower_id)
    flower_id.delete()
    return redirect('flowers_base:flower_data')
```

3.1.4按类别查看

​	在鲜花数据模型内我创建了一个外键指向类别数据的类别id好，这样就可以通过指向类别id号来查看鲜花表中有哪些是这个类的花

```python
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
```

3.1.5搜索视图

​	1）这里我的搜索视图是通过`GET`请求的`get`，也就是`input`输入框内的数据来创建表单，里面填写`input`的`name`，然后再判断搜索的数据是不是数字，是数字就搜索相应的功能，我这里是获取了多个数据，再将多个数据放到一起`modle = list(modle1)+list(modle2)+list(modle3)`，如果不是数字也是相应的操作，如果用户直接点击就会直接显示全部鲜花的内容，我这里是可以搜索全部内容的；另外我`django`中自定义了一个过滤器，使他判断不同数据属于哪个模型，然后显示再相应的位置

```python
def search_flower(request):
    #获取值，这个值是input输入的内容，其中select是input输入框的name
    form = request.GET.get("select",None)
    pattern = "^[0-9]+$"
    #Q是表示可以使用or and这些来搜索
    if form:
        if re.match(pattern, form):
            modle1 = flower_data.objects.filter(
                Q(flower_id=form) | Q(classi=form) | Q(price=form) | Q(num=form))
            modle2 = admin_data.objects.filter(
                Q(admin_id=form)
            )
            modle3 = flower_class.objects.filter(
                Q(class_id=form)
            )
            modle = list(modle1)+list(modle2)+list(modle3)
        else:
            modle1 = flower_data.objects.filter(
                Q(flower_name__icontains=form) | Q(classi__class_name__icontains=form)).order_by('-flower_id').all()
            modle2 = admin_data.objects.filter(
                Q(admin_name__icontains=form)  | Q(telephone__icontains=form)
            )
            modle3 = flower_class.objects.filter(
                Q(class_name__icontains=form)
            )
            modle = list(modle1) + list(modle2)+list(modle3)
    else:
        modle = flower_data.objects.all().order_by('-flower_id')
    # search = flower_data.objects.filter(Q(flower_name__icontains=form) | Q(flower_id__icontains=form) |Q(classi__class_name__icontains=form))
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(modle, 10)
    page_obj = paginator.get_page(page_number)
    # if isinstance(page_obj.object_list[0], flower_data):
    #     n = 1;
    # elif isinstance(page_obj.object_list[0],flower_class):
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
        'key': form
    }
    return render(request,'flowers_base/search.html',context)
```

```html
input代码，这里的input名就为select
 <form class="d-flex " role="search" action="{% url 'flowers_base:search_flower' %}" method="get">
    <div class="mx-auto input-group">
      <input class="form-control form-control-sm" aria-label="Search" type="text" name="select" placeholder="搜索">
       <button class="btn btn-outline-light btn-sm mx-2" type="submit">搜索</button>
     </div>
```





​	2）第二个搜索就是搜索小于输入数量的鲜花列表

`objects.filter(num__lt=form)`表示全部小于这个数字的内容

```python
def search_surplus(request):
    form = request.GET.get('search_surplus')
    pattern = "^[0-9]+$"
    modle = flower_data.objects.all()
    if form and re.match(pattern, form):
            modle = flower_data.objects.filter(num__lt=form)
    page_number = request.GET.get('page', 1) ## 页码
    paginator = Paginator(modle, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': page_number,
    }
    return render(request,'flowers_base/search_surplus.html',context)
```

过滤器代码

```python
from django import template
from django.db.models import Model
from flowers_base.models import admin_data,flower_data,flower_class

register = template.Library()

##查看数据是否为admin_data模型的数据
@register.filter
def isinstanceof_admin(obj):
    return isinstance(obj, admin_data)

##查看数据是否为admin_data模型的数据
@register.filter
def isinstanceof_flower(obj):
    return isinstance(obj, flower_data)

##查看数据是否为admin_data模型的数据
@register.filter
def isinstanceof_class(obj):
    return isinstance(obj, flower_class)


```



##### 2.flower_tanscaction

1）创建模型

​	创建出库表和入库表，表中的鲜花和管理员字段要做外键关联

```python
from django.db import models
from flowers_base.models import flower_class,flower_data,admin_data


# Create your models here.

# 库存信息
# 出库
class outbound(models.Model):
    outbound_id = models.BigIntegerField(unique=True)
    flowers = models.ForeignKey(flower_data,to_field="flower_name", on_delete=models.CASCADE)
    outbound_num = models.IntegerField()
    outbound_date = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(admin_data, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.outbound_id


# 入库
class inbound(models.Model):
    inbound_id = models.BigIntegerField(unique=True)
    flowers = models.ForeignKey(flower_data,to_field="flower_name", on_delete=models.CASCADE)
    inbound_num = models.IntegerField()
    inbound_date = models.DateTimeField(auto_now_add=True)
    # 删除对应管理员后字段设置为NULL
    admin = models.ForeignKey(admin_data, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.inbound_id

```

2）创建form表单

```python
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
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y%m%d%H%M%S")
        instance.outbound_id = formatted_time
        # while True:
        #     new_outbound_id = random.randint(10000, 99999)  # 生成一个随机的四位数作为class_id
        #     if not outbound.objects.filter(outbound_id=new_outbound_id).exists():
        #         instance.outbound_id = new_outbound_id
        #         break
        if commit:
            instance.save()
        return instance

```

3）创建url和视图文件

`url.py`

```python
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
    path('inbound/<int:flower_id>', views.inbound_list, name='inbound'), #入库表视图
    path('outbound/<int:flower_id>', views.outbound_list, name='outbound'), #出库表视图
    path('bound_list/<int:admin_id>',views.admin_bond_list, name='admin_bond_list'), #管理员操作出库入库视图
    path('delete_inbound_data/<int:inbound_id>',views.delete_inbound, name='delete_inbound'), #删除入库视图
    path('delete_outbound_data/<int:outbound_id>',views.delete_outbound, name='delete_outbound'),
    path('bound_list/',views.bond_list, name='bound_list'), #整体出库入库表视图
    # path('in_bound_list/',views.in_bond_list, name='in_bound_list'),
]
```

`view.py`

整体来说和`flowe_base`没有啥区别

```python
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
```

#### 3.2系统测试

##### 1.视图列表

鲜花的视图，从数据库调取数据显示

![image-20231224191451013](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224191451013.png)

鲜花类别视图

![image-20231224191619821](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224191619821.png)

管理员列表视图

![](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224191632663.png)

分别基于`Django`项目`flower`内的`flower_base`应用程序来实现



##### 2.增删改查功能

在每个视图内都增加删除和修改功能，每个视图的增删改查实现方法差不多

###### 2.1修改

选择粉玫瑰，点击修改会跳转到如下视图，**将粉红修改为粉红红**

![image-20231224191921416](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224191921416.png)

![image-20231224221628968](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224221628968.png)

![image-20231224221639835](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224221639835.png)

###### 2.2添加

点击添加鲜花，添加满天星

![image-20231224221753944](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224221753944.png)

![image-20231224221904653](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224221904653.png)

添加了且自动生成了ID

![image-20231224221939310](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224221939310.png)

###### 2.3删除

点击粉红红玫瑰的删除按钮

![image-20231224222102211](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224222102211.png)

再查看就没有了

![image-20231224222127147](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224222127147.png)

###### 2.4查询

查询功能分为了两个查询

1）查询所有

再导航栏内的搜索框搜索1

![image-20231224222519016](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224222519016.png)

查看信息，查看可以搜索到类标号为1的鲜花数据和类别号为一的类别

![image-20231224222543393](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224222543393.png)

搜索20，就可以看见它匹配了编号、单价等

![image-20231224222656684](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224222656684.png)

搜索玫瑰字段

![image-20231224222744645](https://image-1305907375.cos.ap-chengdu.myqcloud.com/Flower_bound_manage_boundimage-20231224222744645.png)