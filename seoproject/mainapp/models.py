from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


STARS = zip(range(1, 6), range(1, 6))


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
    services = models.TextField(
        blank=True,
        verbose_name="Оказываемые услуги"
    )
    rating = models.PositiveIntegerField(
        verbose_name="Цифра рейтинга",
        blank=True
    )
    stars = models.IntegerField(
        default=5,
        choices=STARS,
        verbose_name="Кол-во звезд от 1-5",
        blank=True
    )
    photo = models.ImageField(
        upload_to="clinics/images/",
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
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано"
    )
    tag = TaggableManager()

    def get_absolute_url(self):
        return reverse('show_company', kwargs={'company_slug': self.slug})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['id', 'name']

    def __str__(self):
        return self.name

    @property
    def profit(self):
        company_profit = self.stars * self.rating
        return company_profit


class Reviews(models.Model):
    name = models.CharField(
        verbose_name="ФИО",
        max_length=64,
        unique=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="Отзыв",
        blank=True
    )
    Company = models.ForeignKey(
        "Company",
        related_name="+",
        on_delete=models.CASCADE
    )
    stars = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)],
        verbose_name="Кол-во звезд от 1-5",
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        verbose_name="Электронная почта"
    )
    time_create = models.DateField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    is_published = models.BooleanField(
        default=False, verbose_name="Опубликовано"
    )

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']

    def __str__(self):
        return self.name


class Services(models.Model):
    """
    Справочник услуг клиник
    """
    name = models.CharField(
        verbose_name="Услуга",
        max_length=255,
        unique=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    icon = models.CharField(  # в виде тега, шрифт: https://fontawesome.com/
        verbose_name="Иконка",
        max_length=255,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id', 'name']

    def __str__(self):
        return self.name
