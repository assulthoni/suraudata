from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('work/', views.work, name='work'),
    path('', views.index, name='work')
]
