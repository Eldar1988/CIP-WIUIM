from django.db import models

from django.urls import reverse
from datetime import datetime

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from forum.models import Theme


class AboutReview(models.Model):
    """Отзывы о краудфандинге"""
    name = models.CharField('Имя', max_length=500)
    text = models.TextField('Тексты отзыва или мнения', max_length=2000)
    position = models.CharField('Дополнительно', max_length=500, help_text='Например: должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв или мнение'
        verbose_name_plural = 'Отзывы и мнения'


class Partners(models.Model):
    """Партнеры"""
    name = models.CharField('Название компании', max_length=100)
    logo = models.ImageField('Логотип партнера', upload_to='files/partners/image/',
                                  help_text='В альбомной ориентации')
    url = models.URLField('Ссылка на сайт партнера', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class PartnerForms(models.Model):
    """Формы сотрудничества"""
    title = models.CharField('Заголовок', max_length=100)
    short_description = RichTextUploadingField('Короткоe описание', max_length=200, help_text='Будет выводится на главной странице')
    description = RichTextUploadingField('Полное описание')
    slug = models.SlugField('Slug', unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('partner_forms', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Форма партнерства'
        verbose_name_plural = 'Формы партнерства'


class CompanySocial(models.Model):
    """Социальные сети"""
    name = models.CharField('Название соцсети', max_length=200)
    icon = models.CharField('Иконка', max_length=300)
    url = models.URLField('Ссылка на профиль в сети')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль в соцсети'
        verbose_name_plural = 'Профили в соцсети'


class Company(models.Model):
    """О нас"""
    title = models.CharField('Заголовок - название компании', max_length=200)
    slogan = models.TextField('Слоган - будет на первом экране сайта')
    about_short = RichTextUploadingField('Коротко о краудфандинге', help_text='Будет выводится на главной странице')
    logo = models.ImageField('Логотип компании', upload_to='files/about/image/')
    image = models.ImageField('Картинка компании', upload_to='files/about/image/',
                                  help_text='В хорошем качестве')
    number = models.PositiveIntegerField('Номер телефона')
    address = models.CharField('Адрес компании', max_length=300)
    email = models.EmailField('Email')
    info = RichTextUploadingField('Развернуто о краудфандинге')
    forum_company_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тема на форуме')
    slug = models.SlugField('Slug', unique=True)
    consultant_code = models.TextField('Код консультанта', blank=True)
    right_widget = models.TextField('Виджет в Header', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


class QuestionsAbout(models.Model):
    """Вопросы и ответы о компании"""
    question = models.CharField('Вопрос', max_length=500)
    answer = models.TextField('Ответ', max_length=1000)
    order = models.PositiveSmallIntegerField('Порядковый номер', help_text='Необходим для сортировки вопросов')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ['order']


class Region(models.Model):
    title = models.CharField('Название области или региона', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Map(models.Model):
    x = models.FloatField('Координата Х', null=True)
    y = models.FloatField('Координата y', null=True)
    title = models.CharField('Заголовок', max_length=200)
    map_title = models.CharField('Заголовок для объекта на карте (необязательно)', max_length=200, blank=True)
    short_description = RichTextUploadingField('Краткое описание', help_text='Будет отображаться на карте')
    description = RichTextUploadingField('Полное описание')
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Область')
    slug = models.SlugField('Slug', unique=True)
    pub_date = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('map_object', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты на карте'


class Rules(models.Model):
    """Правила пользования сайтом"""
    title = models.CharField(
        'Заголовок',
        max_length=100,
        help_text='Указать для кого правила. Например: общие или для инвесторов'
    )
    description = RichTextUploadingField(
        'Полное описание'
    )
    slug = models.SlugField(
        'Slug', unique=True, help_text='ВНИМАНИЕ! Если это общие правила, то указать "general", для инвесторов "investor"'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rules', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'
