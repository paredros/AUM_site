# Generated by Django 2.1.2 on 2018-12-05 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20181205_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pagesRelated',
        ),
        migrations.RemoveField(
            model_name='post',
            name='professorRelated',
        ),
        migrations.RemoveField(
            model_name='post',
            name='programRelated',
        ),
    ]