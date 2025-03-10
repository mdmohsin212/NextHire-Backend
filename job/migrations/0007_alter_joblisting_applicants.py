# Generated by Django 5.1.4 on 2024-12-30 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_joblisting_applicants'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='applicants',
            field=models.ManyToManyField(blank=True, limit_choices_to={'profile__role': 'Job Seeker'}, related_name='applied_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
