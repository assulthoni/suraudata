from django.contrib import admin
from blog.models import Post, Category
from martor.widgets import AdminMartorWidget
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
