# Generated by Django 5.1.4 on 2025-01-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_name_jobapplication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='website_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
