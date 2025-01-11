# Generated by Django 5.1.4 on 2025-01-10 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_cart_options_alter_cart_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AddField(
            model_name='review',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-01-01 00:00:00', verbose_name='Дата добавления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default='2025-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]