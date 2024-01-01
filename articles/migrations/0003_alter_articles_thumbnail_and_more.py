# Generated by Django 5.0 on 2024-01-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_content_articles_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='article_thumbnails/'),
        ),
        migrations.AlterField(
            model_name='contentimagesinsidearticles',
            name='image',
            field=models.ImageField(upload_to='article_content_images/'),
        ),
    ]