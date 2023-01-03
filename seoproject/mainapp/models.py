from django.db import models
from django.db.models import Q
from django.urls import reverse
from taggit.managers import TaggableManager


STARS = zip(range(1, 6), range(1, 6))


class CompanyManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(name__iregex=query))
            qs = qs.filter(or_lookup)

        return qs


class Company(models.Model):
    """
    Описание клиник
    """
    name = models.CharField(
        verbose_name="Наименование компании",
        max_length=64,
        unique=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="описание",
        blank=True
    )
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

    objects = CompanyManager()


class Reviews(models.Model):
    """
    Отзывы клиентов
    """

    class Stars(models.IntegerChoices):
        ОТЛИЧНО = 5
        ХОРОШО = 4
        УДОВЛЕТВОРИТЕЛЬНО = 3
        ПЛОХО = 2
        ОТРИЦАТЕЛЬНО = 1

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
    stars = models.IntegerField(
        default=5,
        choices=Stars.choices,
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


class SiteVars(models.Model):
    """
    Переменные сайта
    """
    logo = models.ImageField(
        upload_to="clinics/images/",
        verbose_name="Логотип заголовка"
    )
    head_slogan = models.TextField(
        verbose_name="Слоган сайта",
        max_length=255,
        blank=True
    )
    site_title = models.CharField(
        verbose_name="Заголовок сайта",
        max_length=255,
        blank=True
    )
    meta_tags = models.TextField(
        verbose_name="Мета теги",
        max_length=255,
        blank=True
    )
    site_stat_1 = models.TextField(
        verbose_name="Поле статистики 1",
        max_length=255,
        blank=True
    )
    site_stat_2 = models.TextField(
        verbose_name="Поле статистики 2",
        max_length=255,
        blank=True
    )
    review_slogan = models.TextField(
        verbose_name="Слоган в отзывах",
        max_length=255,
        blank=True
    )
    footer_slogan = models.TextField(
        verbose_name="Слоган футера",
        max_length=255,
        blank=True
    )
    icon_1 = models.CharField(
        verbose_name="Иконка соцсетей 1",
        max_length=255,
        blank=True
    )
    icon_2 = models.CharField(
        verbose_name="Иконка соцсетей 2",
        max_length=255,
        blank=True
    )
    icon_3 = models.CharField(
        verbose_name="Иконка соцсетей 3",
        max_length=255,
        blank=True
    )
    icon_4 = models.CharField(
        verbose_name="Иконка соцсетей 4",
        max_length=255,
        blank=True
    )
    icon_5 = models.CharField(
        verbose_name="Иконка соцсетей 5",
        max_length=255,
        blank=True
    )
    icon_6 = models.CharField(
        verbose_name="Иконка соцсетей 6",
        max_length=255,
        blank=True
    )
    copyright = models.TextField(
        verbose_name="Авторские права",
        max_length=255,
        blank=True
    )
    logo_footer = models.ImageField(
        upload_to="clinics/images/",
        verbose_name="Логотип футера",
        blank=True
    )

    class Meta:
        verbose_name = 'Переменные сайта'
        verbose_name_plural = 'Переменные сайта'
        ordering = ['id']


class TopBanner(models.Model):
    iconbanner = models.ImageField(
        upload_to="topbanner/",
        verbose_name="Иконка банера",
        blank=True
    )
    textup = models.TextField(
        verbose_name="Текст вверху",
        max_length=128,
        blank=True
    )
    textdown = models.TextField(
        verbose_name="Текст внизу",
        max_length=128,
        blank=True
    )

    class Meta:
        verbose_name = 'Верхний баннер'
        verbose_name_plural = 'Верхний баннер'
        ordering = ['id']


class Timetable(models.Model):
    day_week = models.CharField(
        verbose_name='День недели',
        max_length=16,
        blank=True
    )
    time_work = models.CharField(
        verbose_name='Время работы',
        max_length=128,
    blank=True
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['id']


class CompanyPhoto(models.Model):
    photoset = models.ImageField(
        upload_to="clinics/images/",
        verbose_name="Фото"
    )
    description = models.TextField(
        verbose_name="описание",
        blank=True
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано"
    )
    Company = models.ForeignKey(
        "Company",
        related_name="+",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Фото компании'
        verbose_name_plural = 'Фото компаний'
        ordering = ['id']



