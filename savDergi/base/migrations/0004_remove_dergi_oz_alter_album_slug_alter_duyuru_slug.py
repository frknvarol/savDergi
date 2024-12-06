# Generated by Django 5.0.7 on 2024-12-06 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_dergi_sayi_alter_dergi_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dergi',
            name='Oz',
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='duyuru',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
