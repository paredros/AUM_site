# Generated by Django 2.1.2 on 2018-12-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0047_navsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='navsetting',
            name='footerNav',
            field=models.TextField(blank=True, default=''),
        ),
    ]