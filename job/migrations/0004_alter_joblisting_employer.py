# Generated by Django 5.1.4 on 2024-12-29 09:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_categories_categorie'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='employer',
            field=models.ForeignKey(limit_choices_to={'profile__role': 'Employer'}, on_delete=django.db.models.deletion.CASCADE, related_name='job_listing', to=settings.AUTH_USER_MODEL),
        ),
    ]
