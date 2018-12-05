from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.template.defaultfilters import slugify
from aum.models import PageGeneral
from aum.models import Professor
from aum.models import ProgramData


# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    bigPicture = models.ImageField(upload_to='images/blog/', null=True, blank=True)
    summary = models.TextField(max_length=200,default="Enter the summary here...")
    body = RichTextUploadingField(default="", blank=True, config_name='youtube', external_plugin_resources=[(
        'youtube',
        '/static/ckeditor_plugin/ckeditor_youtube/youtube/',
        'plugin.js'
    )])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=False)

    pagesRelated = models.ManyToManyField('aum.PageGeneral')
    professorRelated = models.ManyToManyField('aum.Professor')
    programRelated = models.ManyToManyField('aum.ProgramData')

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug or Post.objects.filter(slug=self.slug).exists():
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']