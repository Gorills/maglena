from django.db import models
from django.urls import reverse
# Create your models here.

class Turn(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
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
    parent = models.ForeignKey(Turn, on_delete=models.CASCADE, related_name='price')

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы'


class Servise(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(upload_to='services')
    text = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey(Turn, on_delete=models.CASCADE, related_name='servise')
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
        