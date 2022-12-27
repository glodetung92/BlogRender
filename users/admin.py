from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'last_login', 'date_joined')
    list_filter = ('email',)
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
