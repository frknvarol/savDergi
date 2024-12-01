# Generated by Django 5.0.7 on 2024-11-29 20:25

import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='name', editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dergi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Duyuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default='topic', editable=False, unique=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='EmbeddedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='DergiKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField()),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dergi')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DergiMakale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dergi')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DergiMakaleText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dergimakale')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DergiSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('source', models.TextField()),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dergi')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DuyuruImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.duyuru')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DuyuruText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.duyuru')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.album')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
