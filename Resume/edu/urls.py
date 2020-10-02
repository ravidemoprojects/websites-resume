from django.urls import path
from . import views

urlpatterns = [
    path('sk/', views.skills, name='skills')
]
