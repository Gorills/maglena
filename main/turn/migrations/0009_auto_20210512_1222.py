# Generated by Django 3.1.7 on 2021-05-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turn', '0008_videoturn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoservises',
            options={'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AlterModelOptions(
            name='videoturn',
            options={'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AddField(
            model_name='videoservises',
            name='autoplay',
            field=models.BooleanField(default=False, null=True, verbose_name='Автопроигрывание'),
        ),
        migrations.AddField(
            model_name='videoservises',
            name='controls',
            field=models.BooleanField(default=False, null=True, verbose_name='Управление видео'),
        ),
        migrations.AddField(
            model_name='videoservises',
            name='mute',
            field=models.BooleanField(default=False, null=True, verbose_name='Звук'),
        ),
        migrations.AddField(
            model_name='videoturn',
            name='autoplay',
            field=models.BooleanField(default=False, null=True, verbose_name='Автопроигрывание'),
        ),
        migrations.AddField(
            model_name='videoturn',
            name='controls',
            field=models.BooleanField(default=False, null=True, verbose_name='Управление видео'),
        ),
        migrations.AddField(
            model_name='videoturn',
            name='mute',
            field=models.BooleanField(default=False, null=True, verbose_name='Звук'),
        ),
    ]
