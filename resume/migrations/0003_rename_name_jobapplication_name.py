# Generated by Django 5.1.4 on 2025-01-02 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_rename_first_name_jobapplication_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='Name',
            new_name='name',
        ),
    ]
