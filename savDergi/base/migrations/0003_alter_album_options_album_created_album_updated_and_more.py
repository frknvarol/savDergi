# Generated by Django 5.0.7 on 2024-12-02 23:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_album_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='album',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dergisayi',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='duyuru',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
