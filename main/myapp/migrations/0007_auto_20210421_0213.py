# Generated by Django 3.1.7 on 2021-04-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_config_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='time',
            field=models.TextField(verbose_name='Время работы'),
        ),
    ]