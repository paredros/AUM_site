# Generated by Django 2.1.2 on 2018-11-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0029_professor_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttonsgeneral',
            name='BasicButton',
            field=models.CharField(default='View', max_length=50),
        ),
    ]
