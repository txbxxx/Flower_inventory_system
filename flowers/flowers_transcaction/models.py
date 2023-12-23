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
