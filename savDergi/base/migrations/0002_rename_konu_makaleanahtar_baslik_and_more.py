# Generated by Django 5.0.7 on 2024-12-08 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makaleanahtar',
            old_name='konu',
            new_name='baslik',
        ),
        migrations.RenameField(
            model_name='makalekaynak',
            old_name='konu',
            new_name='baslik',
        ),
        migrations.RenameField(
            model_name='makaleyazar',
            old_name='konu',
            new_name='baslik',
        ),
        migrations.RemoveField(
            model_name='makale',
            name='konu',
        ),
        migrations.AddField(
            model_name='makale',
            name='baslik',
            field=models.CharField(default='baslik', max_length=100),
        ),
    ]