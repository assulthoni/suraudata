from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('work/', views.work, name='work'),
    path('', views.index, name='work'),
    path('<int:id>', views.get_article, name='work_detail')
]
