# Generated by Django 5.0.7 on 2024-12-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_portre_delete_embeddedvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='portre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='portre',
            name='text',
            field=models.TextField(default='öz geçmiş', max_length=99999),
        ),
        migrations.AlterField(
            model_name='portre',
            name='roportaj',
            field=models.TextField(default='röportaj', max_length=99999),
        ),
    ]