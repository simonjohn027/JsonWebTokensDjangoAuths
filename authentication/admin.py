from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    module = CustomUser


admin.site.register(CustomUser,CustomUserAdmin)