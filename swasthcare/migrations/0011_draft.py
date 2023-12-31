# Generated by Django 4.2.2 on 2023-06-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swasthcare', '0010_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('username', models.CharField(max_length=122, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=122)),
                ('image', models.ImageField(upload_to='media/blog_images')),
                ('category', models.CharField(max_length=122)),
                ('summary', models.CharField(max_length=122)),
                ('content', models.TextField()),
            ],
        ),
    ]
