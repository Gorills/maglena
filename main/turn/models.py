from django.db import models
from django.urls import reverse
# Create your models here.

class Turn(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Короткое описание', null=True)
    image = models.ImageField(upload_to='turn')
    text = models.TextField(verbose_name='Описание услуги')
    meta_title = models.CharField(max_length=200, verbose_name='Мета заголовок')
    meta_description = models.CharField(max_length=300, verbose_name='Мета описание')
    meta_keywords = models.CharField(max_length=200, verbose_name='Ключевые слова')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('turn_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Price(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    text = models.TextField(verbose_name='Прайс')
    parent = models.ForeignKey(Turn, on_delete=models.CASCADE, related_name='price', verbose_name='Категория')

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы'


class Servise(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(upload_to='services')
    text = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey(Turn, on_delete=models.CASCADE, related_name='servise', verbose_name='Категория')
    meta_title = models.CharField(max_length=200, verbose_name='Мета заголовок')
    meta_description = models.CharField(max_length=300, verbose_name='Мета описание')
    meta_keywords = models.CharField(max_length=200, verbose_name='Ключевые слова')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        
        return reverse(
            'servise_list',
            kwargs={'parent': self.parent.slug, 'slug': self.slug}
            )
       

    # def get_absolute_url(self):
    #     return reverse('servise_list', kwargs={'parent': self.parent.slug,'slug': self.slug})

    class Meta:
        verbose_name = 'Доп.услуга'
        verbose_name_plural = 'Доп.услуги'
        

class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='slider', verbose_name='Изображение')
    parent = models.ForeignKey(Turn, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'