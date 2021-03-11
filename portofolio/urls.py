from django.urls import path

from portofolio.views import (index)

urlpatterns = [
    path('', index, name='home'),
]