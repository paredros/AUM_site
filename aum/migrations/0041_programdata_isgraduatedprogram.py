# Generated by Django 2.1.2 on 2018-12-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0040_programdata_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='programdata',
            name='isGraduatedProgram',
            field=models.BooleanField(default=False),
        ),
    ]
