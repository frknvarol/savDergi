# Generated by Django 5.0.7 on 2024-08-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_duyuru_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='duyuru',
            name='block_type',
            field=models.CharField(choices=[('paragraph', 'Paragraph'), ('image', 'Image')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='duyuru',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='duyuru',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='duyuru',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
