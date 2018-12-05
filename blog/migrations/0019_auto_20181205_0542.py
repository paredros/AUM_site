# Generated by Django 2.1.2 on 2018-12-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0056_auto_20181204_2136'),
        ('blog', '0018_auto_20181205_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pagesRelated',
            field=models.ManyToManyField(to='aum.PageGeneral'),
        ),
        migrations.AddField(
            model_name='post',
            name='professorRelated',
            field=models.ManyToManyField(to='aum.Professor'),
        ),
        migrations.AddField(
            model_name='post',
            name='programRelated',
            field=models.ManyToManyField(to='aum.ProgramData'),
        ),
    ]
