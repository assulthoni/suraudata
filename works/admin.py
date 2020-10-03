from django.contrib import admin
from .models import Posts
from django.db import models
from martor.widgets import AdminMartorWidget

# Register your models here.

class PostWidget(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Posts, 
PostWidget
)
