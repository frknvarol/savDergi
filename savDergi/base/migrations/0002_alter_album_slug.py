# Generated by Django 5.0.7 on 2024-12-02 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
