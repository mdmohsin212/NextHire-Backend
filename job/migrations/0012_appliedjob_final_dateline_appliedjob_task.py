# Generated by Django 5.1.4 on 2025-01-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_remove_joblisting_applicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjob',
            name='final_dateline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='task',
            field=models.TextField(blank=True, null=True),
        ),
    ]
