# Generated by Django 4.1.3 on 2022-12-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_company_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Услуга')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('icon', models.CharField(blank=True, max_length=255, verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['id', 'name'],
            },
        ),
    ]