from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()