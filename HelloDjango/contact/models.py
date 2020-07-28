from django.db import models


class Contact(models.Model):
    name = models.CharField('Имя', max_length=200, blank=True)
    phone = models.CharField('Телефон', max_length=100, blank=True)
    email = models.EmailField('Email', max_length=100, blank=True)
    date = models.DateTimeField('Дата и время', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Bot(models.Model):
    number = models.PositiveSmallIntegerField('Номер')
    target = models.CharField('Предназначение', max_length=100)
    name = models.SlugField('Имя бота', max_length=200, unique=True)
    url = models.URLField('URL', unique=True)
    chat_id = models.BigIntegerField('Чат id')
    create_date = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return self.target

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'