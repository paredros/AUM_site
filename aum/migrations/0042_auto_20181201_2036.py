# Generated by Django 2.1.2 on 2018-12-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0041_programdata_isgraduatedprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='programdata',
            name='backgroundColorMini',
            field=models.CharField(default='#CE1731', max_length=7),
        ),
        migrations.AddField(
            model_name='programdata',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
