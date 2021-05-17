# Generated by Django 3.1.7 on 2021-05-12 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turn', '0006_auto_20210422_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoServises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('file', models.FileField(upload_to='video')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='turn.servise', verbose_name='Услуга')),
            ],
        ),
    ]
