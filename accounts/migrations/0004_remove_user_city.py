# Generated by Django 2.2.11 on 2020-04-28 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200428_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
    ]
