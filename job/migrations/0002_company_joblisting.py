# Generated by Django 5.1.4 on 2024-12-29 09:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('requirment', models.TextField()),
                ('loaction', models.CharField(max_length=200)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.categories')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_listing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
