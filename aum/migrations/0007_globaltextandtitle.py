# Generated by Django 2.1.2 on 2018-11-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aum', '0006_auto_20181121_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalTextAndTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitleGeneral', models.CharField(max_length=255)),
            ],
        ),
    ]