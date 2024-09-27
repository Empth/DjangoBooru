# Generated by Django 5.1.1 on 2024-09-27 18:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_alter_imagepost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='imagepost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date'),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='published date'),
        ),
    ]
