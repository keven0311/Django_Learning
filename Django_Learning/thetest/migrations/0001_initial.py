# Generated by Django 4.2.2 on 2024-08-02 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('date', models.DateTimeField(auto_created=True)),
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]