from django.contrib import admin
from .models import inbound,outbound

admin.site.register(inbound)
admin.site.register(outbound)