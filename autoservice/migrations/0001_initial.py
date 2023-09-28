# Generated by Django 3.2.16 on 2023-09-28 05:36

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Укажите адрес автосервиса', max_length=250, verbose_name='Адрес автосервиса')),
                ('rating', models.PositiveSmallIntegerField(help_text='Укажите рейтинг автосервиса', validators=[django.core.validators.MinValueValidator(1, message='Оценка ниже 1 невозможна'), django.core.validators.MaxValueValidator(10, message='Оценка выше 10 невозможна')], verbose_name='Рейтинг автосервиса')),
                ('votes', models.PositiveSmallIntegerField(help_text='Укажите количество отзывов на автосервис', verbose_name='Количество отзывов автосервиса')),
                ('openfrom', models.CharField(help_text='Введите время начала рабочего дня автосервиса в формате HH:MM', max_length=5, null=True, validators=[django.core.validators.RegexValidator('^(?:[01]\\d|2[0-3]):[0-5]\\d$', 'Используйте время в формате HH:MM')], verbose_name='Начало работы')),
                ('openuntil', models.CharField(help_text='Введите время окончания рабочего дня автосервиса в формате HH:MM', max_length=5, null=True, validators=[django.core.validators.RegexValidator('^(?:[01]\\d|2[0-3]):[0-5]\\d$', 'Используйте время в формате HH:MM')], verbose_name='Окончание рабочего дня')),
                ('holidays', models.CharField(choices=[('1', 'Понедельник'), ('2', 'Вторник'), ('3', 'Среда'), ('4', 'Четверг'), ('5', 'Пятница'), ('6', 'Суббота'), ('7', 'Воскресенье')], help_text='Укажите выходной день', max_length=1, null=True, verbose_name='Выходной день')),
                ('phone_number', models.CharField(help_text='Введите номер телефона', max_length=12, null=True, validators=[django.core.validators.RegexValidator('^(\\+7|8)[0-9]{10}$', "Введите номер телефона в формате: '+79995553322'")])),
                ('email', models.EmailField(help_text='Введите адрес электронной почты', max_length=80, null=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='Электронная почта')),
                ('site', models.CharField(help_text="Введите адрес сайта автосервиса в формате 'www.example.com'", max_length=80, null=True, verbose_name='Сайт автосервиса')),
            ],
            options={
                'verbose_name': 'Автосервис',
                'verbose_name_plural': 'Автосервис',
            },
        ),
        migrations.CreateModel(
            name='AutoserviceJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1, message='Стоимость ниже 1 невозможна')], verbose_name='Стоимость работ')),
            ],
            options={
                'verbose_name': 'работу',
                'verbose_name_plural': 'Работы и прайсы автосервисов',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rus_name', models.CharField(max_length=255, verbose_name='Город на русском языке')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города РФ',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите название компании', max_length=250, verbose_name='Название компании по ремонту')),
                ('description', models.TextField(null=True, verbose_name='Описание компании')),
                ('logo', models.ImageField(null=True, upload_to='autoservice/images/logo', verbose_name='Логотип компании')),
                ('legal_address', models.CharField(max_length=250, null=True, verbose_name='Юридический адрес')),
            ],
            options={
                'verbose_name': 'Компания по ремонту авто',
                'verbose_name_plural': 'Компания по ремонту авто',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Оценка ниже 1 невозможна'), django.core.validators.MaxValueValidator(10, message='Оценка выше 10 невозможна')], verbose_name='Оценка автосервиса от пользователя')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='GeolocationAutoService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Значение северной широты на карте')),
                ('longitude', models.FloatField(verbose_name='Значение восточной долготы на карте')),
            ],
            options={
                'verbose_name': 'геолокацию',
                'verbose_name_plural': 'Геолокация автосервисов РФ',
            },
        ),
        migrations.CreateModel(
            name='GeolocationCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Значение северной широты на карте')),
                ('longitude', models.FloatField(verbose_name='Значение восточной долготы на карте')),
            ],
            options={
                'verbose_name': 'геолокацию',
                'verbose_name_plural': 'Геолокация городов РФ',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название работы')),
                ('description', models.CharField(max_length=150, null=True, verbose_name='Описание работы')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
                'ordering': ('title',),
            },
        ),
        migrations.AddConstraint(
            model_name='geolocationcity',
            constraint=models.UniqueConstraint(fields=('latitude', 'longitude'), name='unique_city'),
        ),
        migrations.AddConstraint(
            model_name='geolocationautoservice',
            constraint=models.UniqueConstraint(fields=('latitude', 'longitude'), name='unique_geoservice'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='autoservice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='autoservice.autoservice', verbose_name='Автосервис'),
        ),
        migrations.AddField(
            model_name='city',
            name='geolocation',
            field=models.ForeignKey(help_text='Укажите геолокацию города', on_delete=django.db.models.deletion.CASCADE, to='autoservice.geolocationcity', verbose_name='Геолокация города'),
        ),
        migrations.AddField(
            model_name='autoservicejob',
            name='job',
            field=models.ForeignKey(help_text='Выберите необходимый тип работ', on_delete=django.db.models.deletion.CASCADE, to='autoservice.job', verbose_name='Тип работы автосервиса'),
        ),
        migrations.AddField(
            model_name='autoservicejob',
            name='service',
            field=models.ForeignKey(help_text='Выберите автосервис', on_delete=django.db.models.deletion.CASCADE, to='autoservice.autoservice', verbose_name='Автосервис'),
        ),
    ]
