# Generated by Django 2.1.2 on 2018-11-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0028_auto_20181129_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='skills',
            field=models.TextField(blank=True, default=''),
        ),
    ]