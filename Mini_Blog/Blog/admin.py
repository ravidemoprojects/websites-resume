from django.contrib import admin
from .models import User_post
# Register your models here.

@admin.register(User_post)
class User_admin_post(admin.ModelAdmin):
    list_display =['id','title','desc']
    
    