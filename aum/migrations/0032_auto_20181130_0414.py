# Generated by Django 2.1.2 on 2018-11-30 04:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0031_pagebasic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebasic',
            name='heroTitle',
            field=ckeditor.fields.RichTextField(max_length=100),
        ),
    ]
