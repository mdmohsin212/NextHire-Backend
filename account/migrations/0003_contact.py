# Generated by Django 5.1.4 on 2025-03-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
