# Generated by Django 5.1.4 on 2025-03-05 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0024_rename_loaction_joblisting_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppliedJob',
        ),
    ]
