# Generated by Django 5.0.7 on 2024-08-11 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_album_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='album',
        ),
    ]