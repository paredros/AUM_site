# Generated by Django 2.1.2 on 2018-12-02 23:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0051_auto_20181202_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagebasic',
            name='bottomData',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='topData',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='useBottomData',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='useTopData',
            field=models.BooleanField(default=False),
        ),
    ]
