from django.conf import settings
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)
from django.db import models
from cars.models import Transport


User = get_user_model()


class GeolocationCity(models.Model):
    """
    Модель с геолокацией городов.
    """
    latitude = models.FloatField(
        verbose_name="Значение северной широты на карте",
    )
    longitude = models.FloatField(
        verbose_name="Значение восточной долготы на карте",
    )

    def __str__(self):
        return f"{self.latitude} - {self.longitude}"
    
    class Meta:
        verbose_name = "геолокацию"
        verbose_name_plural = "Геолокация городов РФ"
        constraints = [
            models.UniqueConstraint(
                fields=['latitude', 'longitude'], name='unique_city'
            )
        ]


class City(models.Model):
    """Данные городов с их координатами."""
    rus_name = models.CharField(
        'Город на русском языке',
        max_length=255
    )
    geolocation = models.ForeignKey(
        GeolocationCity,
        on_delete=models.CASCADE,
        verbose_name="Геолокация города",
        help_text="Укажите геолокацию города"
    )

    def __str__(self):
        return f"{self.rus_name}"
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города РФ"


class Company(models.Model):
    """
    Класс для хранения информации о компаниях,
    которые могут производить ремонты автомобилей.
    """
    title = models.CharField(
        max_length=250,
        verbose_name="Название компании по ремонту",
        help_text="Укажите название компании"
    )
    description = models.TextField(
        null=True,
        verbose_name="Описание компании",
    )
    logo = models.ImageField(
        'Логотип компании',
        upload_to='autoservice/images/logo',
        null=True,
    )
    legal_address = models.CharField(
        null=True,
        max_length=250,
        verbose_name="Юридический адрес",
    )

    class Meta:
        verbose_name = "Компания по ремонту авто"
        verbose_name_plural = "Компания по ремонту авто"

    def __str__(self):
        return f"{self.title}"
    

class GeolocationAutoService(models.Model):
    """
    Модель с геолокацией автосервисов.
    """
    latitude = models.FloatField(
        verbose_name="Значение северной широты на карте",
    )
    longitude = models.FloatField(
        verbose_name="Значение восточной долготы на карте",
    )

    def __str__(self):
        return f"{self.latitude} - {self.longitude}"
    
    class Meta:
        verbose_name = "геолокацию"
        verbose_name_plural = "Геолокация автосервисов РФ"
        constraints = [
            models.UniqueConstraint(
                fields=['latitude', 'longitude'], name='unique_geoservice'
            )
        ]


class Job(models.Model):
    """Модель работ"""
    title = models.CharField(
        max_length=settings.MAX_LENGTH_JOBS_NAME,
        verbose_name='Название работы'
    )
    description = models.CharField(
        null=True,
        max_length=settings.MAX_LENGTH_JOBS_DESCRIPTION,
        verbose_name='Описание работы'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.title


class AutoService(models.Model):
    """
    Модель для хранения данных об автосервисах.
    """
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        help_text="Выберите компанию"
    )
    address = models.CharField(
        max_length=250,
        verbose_name="Адрес автосервиса",
        help_text="Укажите адрес автосервиса"
    )
    geolocation = models.ForeignKey(
        GeolocationAutoService,
        on_delete=models.CASCADE,
        verbose_name="Геолокация автосервиса",
        help_text="Укажите геолокацию автосервиса"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Город',
        help_text='Укажите город'
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message='Оценка ниже 1 невозможна'),
            MaxValueValidator(5, message='Оценка выше 5 невозможна')
        ],
        verbose_name='Рейтинг автосервиса',
        help_text='Укажите рейтинг автосервиса'
    )
    votes = models.PositiveSmallIntegerField(
        verbose_name='Количество отзывов автосервиса',
        help_text='Укажите количество отзывов на автосервис'
    )
    openfrom = models.CharField(
        verbose_name='Начало работы',
        null=True,
        max_length=settings.WORKING_TIME_MAX_LENGTH,
        help_text=(
            'Введите время начала рабочего дня автосервиса в формате HH:MM'
        ),
        validators=[
           RegexValidator(
               r'^(?:[01]\d|2[0-3]):[0-5]\d$',
               'Используйте время в формате HH:MM',
           )
        ],
    )
    openuntil = models.CharField(
        verbose_name='Окончание рабочего дня',
        null=True,
        max_length=settings.WORKING_TIME_MAX_LENGTH,
        help_text=(
            'Введите время окончания рабочего дня автосервиса в формате HH:MM'
        ),
        validators=[
           RegexValidator(
               r'^(?:[01]\d|2[0-3]):[0-5]\d$',
               'Используйте время в формате HH:MM',
           )
        ],
    )
    holidays = models.CharField(
        verbose_name='Выходной день',
        help_text=(
            'Укажите выходной день'
        ),
        max_length=1,
        choices=settings.DAY_CHOICES,
        null=True,
    )
    phone_number = models.CharField(
        max_length=settings.PHONE_MAX_LENGTH,
        validators=[
            RegexValidator(
                r'^(\+7|8)[0-9]{10}$',
                "Введите номер телефона в формате: '+79995553322'",
            )
        ],
        help_text="Введите номер телефона",
        null=True,
        #unique=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=settings.EMAIL_MAX_LENGTH,
        null=True,
        #unique=True,
        help_text='Введите адрес электронной почты',
        validators=[ASCIIUsernameValidator()],
        #error_messages={
        #    'unique': 'Автосервис с такой почтой уже существует',
        #},
    )
    site = models.CharField(
        verbose_name='Сайт автосервиса',
        max_length=settings.EMAIL_MAX_LENGTH,
        null=True,
        #unique=True,
        help_text=(
            "Введите адрес сайта автосервиса в формате 'www.example.com'"
        ),
        #validators=[
        #    RegexValidator(
        #        r'^(https?|ftp)://[^\s/$.?#].[^\s]*$$',
        #        message=(
        #            "Ошибка ввода, используйте формат: 'www.example.com'"
        #        )
        #    )
        #],
    )
    job = models.ManyToManyField(
        Job,
        through='autoservicejob',
        verbose_name='Работы',
        help_text='Выберите необходимый тип работ',
    )
    car_service = models.ManyToManyField(
        Transport,
        related_name='autoservices',
        verbose_name='Автомобильные бренды',
        help_text='Выберите автомобильные бренды'
    )

    class Meta:
        verbose_name = "Автосервис"
        verbose_name_plural = "Автосервис"

    def __str__(self):
        return f"{self.company.title} - {self.geolocation}"


class AutoserviceJob(models.Model):
    service = models.ForeignKey(
        AutoService,
        on_delete=models.CASCADE,
        verbose_name='Автосервис',
        help_text='Выберите автосервис',
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        verbose_name='Тип работы автосервиса',
        help_text='Выберите необходимый тип работ',
    )
    price = models.FloatField(
        verbose_name='Стоимость работ',
        validators=[
            MinValueValidator(1, message='Стоимость ниже 1 невозможна'),
        ],
    )

    def __str__(self) -> str:
        return f'{self.job.title} — {self.price}'
    
    class Meta:
        verbose_name = "работу"
        verbose_name_plural = "Работы и прайсы автосервисов"


class Feedback(models.Model):
    '''Отзывы на АвтоСервисы от пользователя.'''
    #author = models.ForeignKey(
    #    User,
    #    on_delete=models.CASCADE,
    #    related_name='feedbacks',
    #    verbose_name='Автор отзыва',
    #)
    autoservice = models.ForeignKey(
        AutoService,
        on_delete=models.CASCADE,
        related_name='feedback',
        verbose_name='Автосервис'
    )
    text = models.TextField(verbose_name='Текст отзыва')
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message='Оценка ниже 1 невозможна'),
            MaxValueValidator(5, message='Оценка выше 5 невозможна')
        ],
        verbose_name='Оценка автосервиса от пользователя'
    )
    pub_date = models.DateTimeField(
        'Дата публикации отзыва',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        #constraints = [
        #    models.UniqueConstraint(
        #        fields=['author', 'autoservice'], name='unique_feedback'
        #    )
        #]

    def __str__(self) -> str:
        return f'{self.text[:25]}'
