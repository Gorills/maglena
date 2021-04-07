from django.db import models

# Create your models here.
class Rewiew(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    text = models.TextField(verbose_name='Отзыв')
    date = models.DateField(auto_now_add=True, verbose_name='Дата отзыва')
    moderate = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    tel = models.CharField(max_length=12, verbose_name='Телефон')
    messages = models.TextField(verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Status(models.Model):
    title = models.CharField(max_length=100, verbose_name='Статус')
    parent = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='status')

    def __str__(self):
        return self.title