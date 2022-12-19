# Generated by Django 4.1.3 on 2022-12-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_topbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_week', models.CharField(blank=True, max_length=16, verbose_name='День недели')),
                ('time_work', models.CharField(blank=True, max_length=128, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='topbanner',
            options={'ordering': ['id'], 'verbose_name': 'Верхний баннер', 'verbose_name_plural': 'Верхний баннер'},
        ),
    ]
