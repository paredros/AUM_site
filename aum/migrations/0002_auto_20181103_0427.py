# Generated by Django 2.1.2 on 2018-11-03 04:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='herobanner',
            name='testImage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='herobanner',
            name='mainText',
            field=ckeditor.fields.RichTextField(),
        ),
    ]