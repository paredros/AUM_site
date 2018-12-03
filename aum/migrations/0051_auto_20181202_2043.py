# Generated by Django 2.1.2 on 2018-12-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0050_buttonsgeneral_talktoadmissionlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroglobaldata',
            name='classicLogo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='heroglobaldata',
            name='useClassicLogo',
            field=models.BooleanField(default=True),
        ),
    ]