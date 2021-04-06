from django.db import models
from djsingleton.models import SingletonModel

# Create your models here.

class Config(SingletonModel):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название компании')
    logo = models.ImageField(upload_to='setup', verbose_name='Логотип')
    time = models.CharField(max_length=150, verbose_name='Время работы')
    email = models.CharField(max_length=100, verbose_name='Почта')
    map = models.TextField(verbose_name='Код карты', null=True, blank=True)

    class Meta:
        verbose_name = 'Общая настройка сайта'
        verbose_name_plural = 'Общие настройки сайта'

class Adres(models.Model):
    adress = models.CharField(max_length=250, verbose_name='Адрес')
    parent = models.ForeignKey(Config, on_delete=models.CASCADE, related_name='adres')
    name = models.CharField(max_length=150, verbose_name='Отображаемое название', null=True)
    phone = models.CharField(max_length=150, verbose_name='Телефон (если есть)', null=True, blank=True)
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Social(models.Model):
    icon = models.CharField(max_length=250, verbose_name='Иконка (fontawesome.com)')
    link = models.CharField(max_length=100, verbose_name='Полная ссылка (с доменным именем)')
    parent = models.ForeignKey(Config, on_delete=models.CASCADE, related_name='social')

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальные сети'


class Phone(models.Model):
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    name = models.CharField(max_length=150, verbose_name='Отображаемое название', null=True)
    parent = models.ForeignKey(Config, on_delete=models.CASCADE, related_name='phone')
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'



class Meta(SingletonModel):
    meta_title = models.CharField(max_length=200, verbose_name='Мета заголовок')
    meta_description = models.CharField(max_length=350, verbose_name='Мета описание')
    meta_subtitle = models.CharField(max_length=150, verbose_name='Вторая часть заголовка сайта (через | )')
    meta_keywords = models.CharField(max_length=350, verbose_name='Ключевые слова')
    domen = models.CharField(max_length=350, verbose_name='Полный адрес сайта')

    class Meta:
        verbose_name = 'Мета настройка сайта'
        verbose_name_plural = 'Мета настройки сайта'

class Vacancy(SingletonModel):
    text = models.TextField(verbose_name='Текст на страницу вакансий')
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class Worker(models.Model):
    name = models.CharField(max_length=150, verbose_name='Фио')
    image = models.ImageField(upload_to='workers', verbose_name='Фотография')
    position = models.CharField(max_length=350, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Awards(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='awards')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сертификат или награда'
        verbose_name_plural = 'Сертификаты или награды'
