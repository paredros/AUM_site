# Generated by Django 2.1.2 on 2018-12-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0046_auto_20181201_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topNavBar', models.TextField(blank=True, default='')),
            ],
        ),
    ]
