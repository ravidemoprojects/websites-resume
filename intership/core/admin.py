from django.contrib import admin
from .models import Doubt
# Register your models here.

@admin.register(Doubt)
class DoubtModelAdmin(admin.ModelAdmin):
    list_display= ['id','subject','desc']