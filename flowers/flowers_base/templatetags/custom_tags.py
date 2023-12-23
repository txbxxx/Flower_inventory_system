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

