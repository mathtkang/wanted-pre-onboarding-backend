# Generated by Django 4.2.6 on 2023-10-18 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_user_is_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
