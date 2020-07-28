from django.db import models
from django.urls import reverse
from datetime import datetime

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Theme(models.Model):
    """Тема"""
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=User, null=True, verbose_name='Автор')
    title = models.CharField('Заголовок темы', max_length=500)
    preview = models.TextField('Отрывок', max_length=700)
    body = RichTextUploadingField('Тело темы (Начало не должно иметь быть заголовком или картинкой - только обычное форматирование)')
    url = models.SlugField('URL темы', max_length=100, unique=True)
    draft = models.BooleanField('Опубликовать?', default=True)
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)
    like = models.PositiveSmallIntegerField('Количество лайков', default=0)
    show_count = models.PositiveSmallIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('theme_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['-pub_date']


class Comment(models.Model):
    """Ответ на форуме"""
    email = models.EmailField()
    name = models.CharField('Имя автора', max_length=100)
    text = RichTextUploadingField('Сообщение', max_length=7000)
    theme = models.ForeignKey(Theme, verbose_name='Тема', on_delete=models.CASCADE)
    answer_for = models.ForeignKey('self', verbose_name='Ответ на сообщение от', on_delete=models.SET_NULL, blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now, blank=True)
    draft = models.BooleanField('Опубликовать?', default=True)
    like = models.PositiveSmallIntegerField('Количество лайков', default=0)

    def __str__(self):
        return f"{self.name} - {self.theme}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-pub_date']
