# Generated by Django 2.1.2 on 2018-12-04 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0055_newslettercontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applybanner',
            options={'verbose_name_plural': 'APPLY Banner Data'},
        ),
        migrations.AlterModelOptions(
            name='bloggeneral',
            options={'verbose_name_plural': 'BLOG General Data'},
        ),
        migrations.AlterModelOptions(
            name='contactwebpage',
            options={'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='newslettercontact',
            options={'verbose_name_plural': 'Newsletter'},
        ),
        migrations.AlterModelOptions(
            name='programdata',
            options={'verbose_name_plural': 'Programs Data'},
        ),
    ]