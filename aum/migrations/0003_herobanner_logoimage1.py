# Generated by Django 2.1.2 on 2018-11-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0002_auto_20181103_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='herobanner',
            name='logoImage1',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]