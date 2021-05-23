from django.urls import path
from django.urls import path, include
from portofolio.views import (index)

urlpatterns = [
    path('', index, name='home'),
    path('blog/', include('blog.urls'), name='blog'),
]