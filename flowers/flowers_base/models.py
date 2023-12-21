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
