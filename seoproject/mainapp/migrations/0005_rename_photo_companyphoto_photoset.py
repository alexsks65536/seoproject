# Generated by Django 4.1.3 on 2023-01-01 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_reviews_stars_companyphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyphoto',
            old_name='photo',
            new_name='photoset',
        ),
    ]
