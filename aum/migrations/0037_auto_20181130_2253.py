# Generated by Django 2.1.2 on 2018-11-30 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0036_auto_20181130_0525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagebasic',
            options={'verbose_name_plural': 'Generals Page Edition'},
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='colorBackTop',
            field=models.CharField(default='#E9EAE4', max_length=7),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='colorTextTop',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='tintOverlayTop',
            field=models.FloatField(default=0.7, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='useBackColorTop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='useImageTop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagebasic',
            name='useVideoTop',
            field=models.BooleanField(default=True),
        ),
    ]