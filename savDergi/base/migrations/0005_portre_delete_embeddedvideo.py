# Generated by Django 5.0.7 on 2024-12-13 05:07

import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_makalekaynak_options_alter_makaleyazar_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(default='Başlık', max_length=100)),
                ('roportaj', models.TextField(default='röportaj')),
                ('link', models.URLField(default='https://open.spotify.com/show/2HE4WPETsojDxh9GRFIiZP?si=8cf043f5e13d41bb')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='EmbeddedVideo',
        ),
    ]