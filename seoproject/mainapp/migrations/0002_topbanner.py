# Generated by Django 4.1.3 on 2022-12-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iconbanner', models.ImageField(blank=True, upload_to='topbanner/', verbose_name='Иконка банера')),
                ('textup', models.TextField(blank=True, max_length=128, verbose_name='Текст вверху')),
                ('textdown', models.TextField(blank=True, max_length=128, verbose_name='Текст внизу')),
            ],
            options={
                'verbose_name': 'Верхний баннер',
                'verbose_name_plural': 'Верхнего баннера',
                'ordering': ['id'],
            },
        ),
    ]
