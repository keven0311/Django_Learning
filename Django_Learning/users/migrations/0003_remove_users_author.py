# Generated by Django 5.0.7 on 2024-08-06 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='author',
        ),
    ]
