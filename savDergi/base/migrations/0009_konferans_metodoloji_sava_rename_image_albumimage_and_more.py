# Generated by Django 5.0.7 on 2024-12-13 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_portre_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konferans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(default='Başlık', max_length=100)),
                ('text', models.TextField(default='konferans text', max_length=99999)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Metodoloji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(default='Metodoloji başlık', max_length=100)),
                ('text', models.TextField(default='metodoloji text', max_length=99999)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Sava',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(default='SAVA başlık', max_length=100)),
                ('text', models.TextField(default='SAVA text', max_length=99999)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.RenameModel(
            old_name='Image',
            new_name='AlbumImage',
        ),
        migrations.AddField(
            model_name='portre',
            name='slug',
            field=models.SlugField(default='slug', editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='KonferansImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('baslik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.konferans')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='MetodolojiImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('baslik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.metodoloji')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SavaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('baslik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sava')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
