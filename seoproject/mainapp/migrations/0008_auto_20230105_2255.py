# Generated by Django 4.1.3 on 2023-01-05 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_price_options_alter_price_price_and_more'),
    ]

    operations = [
        migrations.RenameField('Price', 'price', 'price_min'),
    ]
