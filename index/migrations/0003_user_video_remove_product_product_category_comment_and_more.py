# Generated by Django 5.1.2 on 2024-10-24 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_product_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('password2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=128)),
                ('video_content', models.ImageField(upload_to='media')),
                ('user', models.TextField()),
                ('like', models.TextField()),
                ('dislike', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comment_user', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.video')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
