from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    telephone = models.CharField(max_length=16, verbose_name="Телефон")
    address = models.TextField(blank=True, verbose_name="Адрес")
    nearest_metro_stations = models.TextField(blank=True, verbose_name="Ближайшая станция метро")
    opening_hours = models.TextField(blank=True, verbose_name="Часы работы")
    services = models.TextField(blank=True, verbose_name="Сервис")
    review = models.ImageField(blank=True, verbose_name="Отзывы")
    rating = models.ImageField(blank=True, verbose_name="Рейтинг")
    stars = models.ImageField(blank=True, verbose_name="Звезды")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateField(auto_now=True, verbose_name="Время изменения")
    # revs = models.ForeignKey('Reviews', on_delete=models.PROTECT, verbose_name="Отзывы")

    def __str__(self):
        return self.name  # возвращает заголовок текущей записи

    def get_absolute_url(self):
        """
        Формирует абсолютный url для шаблона
        :return:
        """
        return reverse('company', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['time_create', 'name']


class Reviews(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    stars = models.ImageField(blank=True, verbose_name="Звезды")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email")
    company = models.ForeignKey('Company', on_delete=models.PROTECT, verbose_name="Компания")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Формирует абсолютный url для шаблона
        :return:
        """
        return reverse('reviews', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']
