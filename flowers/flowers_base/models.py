from django.db import models

# Create your models here.

#鲜花类别模型
class flower_class(models.Model):
    #定义类别号、类别名称
    class_id   = models.IntegerField(primary_key = True)
    class_name = models.CharField(max_length=30)


#定义鲜花模型
class flower_data(models.Model):
    #定义编号、名称、类别号、单价、库存数
    flower_id   =  models.IntegerField(primary_key = True)
    flower_name =  models.CharField(max_length=20)
    #设置外键指向flower_class，如果flower_class删除关于这个类别的所有鲜花也都删除
    classi      =  models.ForeignKey(flower_class,on_delete=models.CASCADE)
    price       =  models.IntegerField(null=True)
    num         =  models.IntegerField()

#管理员模型
class admin_data(models.Model):
    #定义管理员工号、姓名、电话
    admin_id   = models.IntegerField(primary_key = True)
    admin_name = models.CharField(max_length=30)
    telephone  = models.CharField(max_length=30,null=True)


