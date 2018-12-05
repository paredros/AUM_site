from django.contrib import admin
from .models import *
from django.template.defaultfilters import slugify

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def _get_unique_slug(self, obj):
        slug = slugify(obj.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save_model(self, request, obj, form, change):
        if Post.objects.filter(slug=obj.slug).exists():
            obj.slug = self._get_unique_slug(obj)
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)