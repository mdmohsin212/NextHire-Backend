# Generated by Django 5.1.4 on 2025-02-16 09:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_jobapplication_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cv',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='file'),
        ),
    ]
