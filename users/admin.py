from django.contrib import admin
from .models import User


class userPanel (admin.ModelAdmin) : 
    list_display = ['full_name','email','is_gold','id']

admin.site.register(User, userPanel)