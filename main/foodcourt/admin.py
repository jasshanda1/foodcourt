from django.contrib import admin
from .models import Info, Order, User
admin.site.register(User)
admin.site.register(Info)
admin.site.register(Order)