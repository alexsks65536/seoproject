from django.db import models
from django.urls import reverse


class Company(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    prod = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name="Продукт")

    def __str__(self):
        return self.title  # возвращает заголовок текущей записи

    def get_absolute_url(self):
        """
        Формирует абсолютный url для шаблона
        :return:
        """
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ['time_create', 'title']


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Формирует абсолютный url для шаблона
        :return:
        """
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
