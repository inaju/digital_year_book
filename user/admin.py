from django.contrib import admin
from .models import *
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['email','Matno']
    list_display = ['email','Matno','Regno','college','department','program']
    list_filter = ['college','department','program']
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(College)
