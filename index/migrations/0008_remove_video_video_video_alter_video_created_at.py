# Generated by Django 5.1.2 on 2024-10-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_video',
        ),
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateField(),
        ),
    ]