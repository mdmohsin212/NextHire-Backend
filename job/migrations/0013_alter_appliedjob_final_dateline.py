# Generated by Django 5.1.4 on 2025-01-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_appliedjob_final_dateline_appliedjob_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedjob',
            name='final_dateline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
