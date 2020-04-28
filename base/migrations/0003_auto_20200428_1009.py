# Generated by Django 2.2.11 on 2020-04-28 10:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_filemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='filemodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
