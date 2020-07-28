from django.db import models
from django.urls import reverse
from datetime import datetime

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from forum.models import Theme
from user.models import Company


class Data(models.Model):
    """цифровые показатели"""
    name = models.CharField('Наименование показателя', max_length=300)
    number = models.CharField('Значение', max_length=30, help_text='Например, 80%')
    deta_int = models.PositiveSmallIntegerField('Значение шкалы', default=0, help_text='Значение шкалы от 1 до 100')
    order = models.PositiveSmallIntegerField('Порядковый номер', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'
        ordering = ['order']


class Benefits(models.Model):
    """Преимущества проекта"""
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Описание')
    icon = models.TextField('Иконка', help_text='Выбрать на сайте https://www.icofont.com/icons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Structure(models.Model):
    """Структура проекта"""
    title = models.CharField('Заголовок', max_length=200)
    short_title = models.CharField('Короткий заголовок', max_length=100,
                                   help_text='Заголовок, который будет под иконкой')
    icon = models.TextField('Иконка', help_text='Выбрать на сайте https://www.icofont.com/icons')
    short_description = RichTextUploadingField('Короткое описание', max_length=2000, help_text='Будет на странице проекта')
    short_description_seo = models.TextField('Описание для CEO (необязательно)', max_length=500, blank=True)
    description = RichTextUploadingField('Полное описание')
    slug = models.SlugField('Slug', max_length=100, unique=True, help_text='Ссылка. Писать на латинице и без пробелов _')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    image = models.ImageField('Картинка', upload_to='files/project/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('structure_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Структура проекта'
        ordering = ['order']


class Questions(models.Model):
    question = models.CharField('Вопрос', max_length=500)
    answer = models.TextField('Ответ', max_length=1000)
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Необходим для сортировки вопросов')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ['order']


class Review(models.Model):
    name = models.CharField('Имя', max_length=500)
    text = models.TextField('Тексты отзыва или мнения', max_length=2000)
    position = models.CharField('Дополнительно', max_length=500, help_text='Например: должность')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Отзыв или мнение'
        verbose_name_plural = 'Отзывы и мнения'


class Project(models.Model):
    """Тема"""
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, default=User, null=True, verbose_name='Компания')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=User, null=True, verbose_name='Пользователь')
    name = models.CharField('Название проекта', max_length=200)
    short_description = models.TextField('Краткое описание проекта', max_length=700,
                                         help_text='Будет отображаться в списке проектов')
    title = models.CharField('Заголовок проекта', max_length=200, help_text='Заголовок черного цвета')
    title_grey = models.CharField('Заголовок проекта серый', max_length=200, help_text='Заголовок серого цвета')
    body = models.TextField('Крaткое описание проекта', max_length=700,
                                         help_text='Будет отображаться в списке проектов')
    description_first_title = models.CharField('Описание 1 - Заголовок', max_length=30)
    description_first = RichTextUploadingField('Описание 1', max_length=2000)
    description_second_title = models.CharField('Описание 2 - Заголовок', max_length=30)
    description_second = RichTextUploadingField('Описание 2', max_length=2000)
    video_title = models.CharField('Заголовок для блока видео', max_length=300)
    video_url = models.URLField('Ссылка на видео', max_length=200)
    benefits = models.ManyToManyField(Benefits, blank=True, verbose_name='Преимуществa')
    data = models.ManyToManyField(Data, blank=True, verbose_name='Показатели',
                                  related_name='title')
    structure_element = models.ManyToManyField(Structure,
                                               verbose_name='Структура проекта')
    questions = models.ManyToManyField(Questions, blank=True,
                                               verbose_name='Вопросы и ответы')
    reviews = models.ManyToManyField(Review, blank=True,
                                               verbose_name='Отзывы или мнения')
    order = models.PositiveSmallIntegerField('Порядковый номер проекта', blank=False,
                                             help_text='Необходим для сортировки проектов')
    slug = models.SlugField('Slug проекта', max_length=100, unique=True,
                            help_text='Должен быть уникальным, только на латинице, вместо пробелов использовать _')
    forum_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тема на форуме')
    draft = models.BooleanField('Опубликовать?', default=True)
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)
    show_count = models.PositiveSmallIntegerField('Количество просмотров', default=0)
    image = models.ImageField('Картинка проекта', upload_to='files/project/',
                              help_text='Будет отображаться в списке проектов')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['order']
