# Generated by Django 2.1.2 on 2018-11-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0018_programdata_futureblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='programdata',
            name='futureBlock_keys',
            field=models.TextField(default=''),
        ),
    ]
