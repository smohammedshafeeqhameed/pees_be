from django.contrib import admin
from .models import *
# Register your models here.
class SleepMythAdmin(admin.ModelAdmin):
    list_display = ('myth', 'fact')  # Specify the fields you want to display in the admin list

admin.site.register(SleepMyth, SleepMythAdmin)