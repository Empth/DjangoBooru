# Generated by Django 5.1.1 on 2024-09-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_alter_imagepost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
