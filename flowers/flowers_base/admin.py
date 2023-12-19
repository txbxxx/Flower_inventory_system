from django.contrib import admin

from .models import flower_class,admin_data,flower_data
# Register your models here.
admin.site.register(flower_class)
admin.site.register(admin_data)
admin.site.register(flower_data)