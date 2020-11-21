from django.contrib import admin
from .models import Catogory, Products, Customers
# Register your models here.

@admin.register(Catogory)
class AdminCatogory(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ['id','name','price','catogory','desc','image']


@admin.register(Customers)
class AdminCustomers(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone_number','email','password']