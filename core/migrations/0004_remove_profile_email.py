# Generated by Django 5.0.2 on 2024-02-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
