# Generated by Django 4.1.3 on 2023-01-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_price_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]