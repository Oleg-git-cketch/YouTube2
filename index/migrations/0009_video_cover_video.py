# Generated by Django 5.1.2 on 2024-10-26 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_remove_video_video_video_alter_video_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cover_video',
            field=models.FileField(default=datetime.datetime(2024, 10, 26, 7, 33, 51, 779250, tzinfo=datetime.timezone.utc), upload_to='videos/'),
            preserve_default=False,
        ),
    ]
