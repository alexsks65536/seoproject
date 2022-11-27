from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


# class Company(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Заголовок")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     content = models.TextField(blank=True, verbose_name="Текст статьи")
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
#     time_create = models.DateField(auto_now_add=True, verbose_name="Время создания")
#     time_update = models.DateField(auto_now=True, verbose_name="Время изменения")
#     is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
#     prod = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name="Продукт")
#
#     def __str__(self):
#         return self.title  # возвращает заголовок текущей записи
#
#     def get_absolute_url(self):
#         """
#         Формирует абсолютный url для шаблона
#         :return:
#         """
#         return reverse('post', kwargs={'post_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Компания'
#         verbose_name_plural = 'Компании'
#         ordering = ['time_create', 'title']
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         """
#         Формирует абсолютный url для шаблона
#         :return:
#         """
#         return reverse('category', kwargs={'cat_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#         ordering = ['id']
#


class Company(models.Model):
    name = models.CharField(verbose_name="Наименование компании", max_length=64, unique=True, blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    telephone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    address = models.TextField(blank=True, verbose_name="Адрес коммпании")
    nearest_metro_stations = models.TextField(blank=True, verbose_name="Ближайшие метро")
    opening_hours = models.TextField(blank=True, verbose_name="Режим работы")
    services = models.TextField(blank=True, verbose_name="Оказываемые услуги")
    reviews = models.IntegerField(verbose_name="Кол-во отзывов", blank=True)
    rating = models.IntegerField(verbose_name="Цифра рейтинга", blank=True)
    stars = models.IntegerField(verbose_name="Кол-во звезд от 1-5", blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=64, unique=True, blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    Company = models.ForeignKey("Company", related_name="+", on_delete=models.CASCADE)
    stars = models.IntegerField(verbose_name="Кол-во звезд от 1-5", blank=True)
    email = models.EmailField(max_length=254, verbose_name="электронная почта")

    def __str__(self):
        return self.name
