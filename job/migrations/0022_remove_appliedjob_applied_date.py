# Generated by Django 5.1.4 on 2025-02-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0021_appliedjob_applied_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='applied_date',
        ),
    ]
