# Generated by Django 5.0.7 on 2024-08-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_duyuru_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='duyuru',
            name='slug',
            field=models.SlugField(default='topic', editable=False, unique=True),
        ),
    ]
