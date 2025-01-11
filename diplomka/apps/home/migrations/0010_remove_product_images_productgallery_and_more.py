# Generated by Django 5.1.4 on 2025-01-09 09:24

import apps.home.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_productimage_remove_product_images_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_product', models.ImageField(upload_to=apps.home.models.product_gallery_image_path, verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product', verbose_name='Пост')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
