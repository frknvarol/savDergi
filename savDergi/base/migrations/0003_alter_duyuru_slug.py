# Generated by Django 5.0.7 on 2024-08-03 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_duyuru_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duyuru',
            name='slug',
            field=models.SlugField(default=False, max_length=200, unique=True),
        ),
    ]
