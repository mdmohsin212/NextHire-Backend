# Generated by Django 5.1.4 on 2025-02-09 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_alter_appliedjob_is_complete'),
        ('payment', '0005_alter_checkout_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.appliedjob'),
        ),
    ]
