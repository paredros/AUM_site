# Generated by Django 2.1.2 on 2018-12-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0039_auto_20181130_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='programdata',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]