from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class Company(models.Model):
    name = models.CharField(
        verbose_name="Наименование компании",
        max_length=64,
        unique=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="описание",
        blank=True)
    phoneNumberRegex = RegexValidator(
        regex=r"^\+?1?\d{8,15}$"
    )
    telephone = models.CharField(
        validators=[phoneNumberRegex],
        max_length=16,
        unique=True
    )
    address = models.TextField(
        blank=True,
        verbose_name="Адрес коммпании"
    )
    nearest_metro_stations = models.TextField(
        blank=True,
        verbose_name="Ближайшие метро"
    )
    opening_hours = models.TextField(
        blank=True,
        verbose_name="Режим работы"
    )
    services = models.TextField(
        blank=True,
        verbose_name="Оказываемые услуги"
    )
    reviews = models.IntegerField(
        verbose_name="Кол-во отзывов",
        blank=True
    )
    rating = models.IntegerField(
        verbose_name="Цифра рейтинга",
        blank=True
    )
    stars = models.IntegerField(
        verbose_name="Кол-во звезд от 1-5",
        blank=True
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Фото"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    time_create = models.DateField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    time_update = models.DateField(
        auto_now=True,
        verbose_name="Время изменения"
    )

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name = models.CharField(
        verbose_name="ФИО",
        max_length=64,
        unique=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="описание",
        blank=True
    )
    Company = models.ForeignKey(
        "Company",
        related_name="+",
        on_delete=models.CASCADE
    )
    stars = models.IntegerField(
        verbose_name="Кол-во звезд от 1-5",
        blank=True
    )
    email = models.EmailField(
        max_length=254,
        verbose_name="электронная почта"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name