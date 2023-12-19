from django.db import models
from flowers_base.models import flower_class,admin_data

# Create your models here.

#库存信息
#出库
class outbound(models.Model):
    outbound_id   = models.IntegerField()
    flowers    = models.ForeignKey(flower_class,on_delete=models.CASCADE)
    outbound_num  = models.IntegerField()
    outbound_date = models.DateTimeField(auto_now_add=True)
    admin      = models.ForeignKey(admin_data,on_delete=models.SET_NULL,null=True)

#入库
class inbound(models.Model):
    inbound_id    = models.IntegerField()
    flowers    = models.ForeignKey(flower_class,on_delete=models.CASCADE)
    inbound_num   = models.IntegerField()
    inbound_date  = models.DateTimeField(auto_now_add=True)
    #删除对应管理员后字段设置为NULL
    admin      = models.ForeignKey(admin_data,on_delete=models.SET_NULL,null=True)