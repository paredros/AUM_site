from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    bigPicture = models.ImageField(upload_to='images/blog/', null=True, blank=True)
    summary = models.TextField(max_length=200,default="Enter the summary here...")
    body = RichTextUploadingField(default="", blank=True, config_name='youtube', external_plugin_resources=[(
        'youtube',
        '/static/ckeditor_plugin/ckeditor_youtube/youtube/',
        'plugin.js'
    )])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug
