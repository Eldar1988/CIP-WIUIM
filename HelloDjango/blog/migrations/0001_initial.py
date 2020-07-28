# Generated by Django 3.0.7 on 2020-06-11 18:47

import ckeditor_uploader.fields
import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок категории')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='URL категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Заголовок поста')),
                ('preview', models.TextField(max_length=700, verbose_name='Отрывок')),
                ('miniature', models.ImageField(help_text='Рекомендуемые размер 370х370 пикселов', upload_to='files/posts/miniatures/', verbose_name='Миниатюра поста')),
                ('image', models.ImageField(help_text='Рекомендуемые размер 1920x600 пикселов', upload_to='files/posts/image/', verbose_name='Картинка поста')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Тело поста')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='URL поста')),
                ('draft', models.BooleanField(default=False, verbose_name='Опубликовать?')),
                ('recommend', models.BooleanField(default=False, verbose_name='Рекомендуем?')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('like', models.PositiveSmallIntegerField(default=0, verbose_name='Количество лайков')),
                ('dislike', models.PositiveSmallIntegerField(default=0, verbose_name='Количество дислайков')),
                ('show_count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество просмотров')),
                ('author', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='Категория поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='ip адрес')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Пост')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.RatingStar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=3000, verbose_name='Комментарий')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Comment', verbose_name='Родитель')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
