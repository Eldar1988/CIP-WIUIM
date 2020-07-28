from django.db import models
from django.urls import reverse
from datetime import datetime

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """Категория постов"""
    title = models.CharField('Заголовок категории', max_length=200)
    url = models.SlugField('URL категории', max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Пост"""
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=User, null=True, verbose_name='Автор', related_name='post_author')
    title = models.CharField('Заголовок поста', max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория поста', blank=True, null=True, related_name='post_category')
    preview = models.TextField('Отрывок', max_length=700)
    miniature = models.ImageField('Миниатюра поста', upload_to='files/posts/miniatures/',
                                  help_text='Рекомендуемые размер 370х370 пикселов')
    image = models.ImageField('Картинка поста', upload_to='files/posts/image/',
                                  help_text='Рекомендуемые размер 1920x600 пикселов')
    body = RichTextUploadingField('Тело поста (Начало не должно иметь быть заголовком или картинкой - только обычное форматирование)')
    url = models.SlugField('URL поста', max_length=100, unique=True)
    draft = models.BooleanField('Опубликовать?', default=False)
    recommend = models.BooleanField('Рекомендуем?', default=False)
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)
    post_rating = models.PositiveSmallIntegerField('Рэйтинг', null=True, help_text='от 1 до 7')
    like = models.PositiveSmallIntegerField('Количество лайков', default=0)
    dislike = models.PositiveSmallIntegerField('Количество дислайков', default=0)
    show_count = models.PositiveSmallIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.url})

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя автора', max_length=100)
    text = models.TextField('Комментарий', max_length=3000)
    parent = models.ForeignKey('self', verbose_name='Ответ на комментарий', on_delete=models.SET_NULL, blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE, related_name='comment_post')
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)
    draft = models.BooleanField('Опубликовать?', default=True)

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
