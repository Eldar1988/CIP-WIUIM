# Generated by Django 3.0.7 on 2020-06-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200610_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='profile',
            name='fb',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Ссылка на профиль Facebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Ссылка на профиль Instagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=500, verbose_name='ФИО или название компании'),
        ),
        migrations.AddField(
            model_name='profile',
            name='register_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата регистрации'),
        ),
        migrations.AddField(
            model_name='profile',
            name='slogan',
            field=models.TextField(blank=True, max_length=500, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='profile',
            name='vk',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Ссылка на профиль ВКонтакте'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=30, verbose_name='Информация о пользователе'),
        ),
    ]
