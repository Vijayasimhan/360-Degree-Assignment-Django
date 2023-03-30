from django.contrib import admin
from .models import Users
# Register your models here.
@admin.register(Users)
class AdminUser(admin.ModelAdmin):
    list_display=["name", "id", "contact", "address"]