# Generated by Django 4.2.16 on 2024-12-05 09:20

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=recipe.models.create_path_to_upload, verbose_name='Изображение блюда'),
        ),
    ]
