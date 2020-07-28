from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    """User дополнения"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)
    name = models.CharField('ФИО', max_length=500)
    main_phone = models.CharField('Основной номер телефона', max_length=30, blank=True,
                                  help_text='Указывать необязательно. Будет публиковано на сайте')
    second_phone = models.CharField('Дополнительный номер телефона (необязательно)', max_length=30, blank=True,
                                    help_text='Указывать необязательно. Будет публиковано на сайте')
    whatsapp_phone = models.CharField('Номер Whatapp (необязательно)', max_length=30, blank=True,
                                      help_text='Необходимо вместо +7 или 8 указать просто 7. '
                                                'Указывать номер обязательно без пробелов тире и других знаков ')
    mail = models.EmailField('E-mail', blank=True)
    slogan = models.TextField('Слоган', max_length=500)
    bio = RichTextUploadingField('Информация о пользователе')
    professional = models.CharField('Профессия', max_length=200)
    register_date = models.DateTimeField('Дата регистрации', auto_now_add=True, null=True, blank=True)
    vk = models.URLField('Ссылка на профиль ВКонтакте', max_length=200, blank=True)
    fb = models.URLField('Ссылка на профиль Facebook', max_length=200, blank=True)
    instagram = models.URLField('Ссылка на профиль Instagram', max_length=200, blank=True)
    url = models.SlugField('URL', default=User, unique=True)
    avatar = models.ImageField('Аватар', upload_to='files/users/avatars/', help_text='250x250px')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-register_date']


class Company(models.Model):
    """Компания"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Администратор компании на сайте', null=True)
    name = models.CharField('Название компании', max_length=500, null=True)
    name_legal = RichTextUploadingField('Реквизиты компании', blank=True)
    address = models.CharField('Адрес компании', max_length=500)
    main_phone = models.CharField('Основной номер телефона', max_length=30, blank=True)
    second_phone = models.CharField('Дополнительный номер телефона (необязательно)', max_length=30, blank=True)
    whatsapp_phone = models.CharField('Номер Whatapp (необязательно)', max_length=30, blank=True,
                                      help_text='Необходимо вместо +7 или 8 указать просто 7. Указывать номер обязательно без пробелов тире и других знаков ')
    mail = models.EmailField('E-mail', blank=True)
    slogan = models.TextField('Слоган', max_length=500)
    about_cooperators = models.TextField('Несколько слов о Вашей команде сотрудников (если она есть)', blank=True)
    bio = RichTextUploadingField('Информация о компании', blank=True)
    specialization = models.CharField('Специализация', max_length=200)
    cooperator = models.ManyToManyField(Profile, verbose_name='Сотрудники', blank=True)
    register_date = models.DateTimeField('Дата регистрации', auto_now_add=True, null=True, blank=True)
    vk = models.URLField('Ссылка на профиль ВКонтакте', max_length=200, blank=True)
    fb = models.URLField('Ссылка на профиль Facebook', max_length=200, blank=True)
    instagram = models.URLField('Ссылка на профиль Instagram', max_length=200, blank=True)
    url = models.SlugField('URL', default=User, unique=True)
    logo = models.ImageField('Логотип', upload_to='files/company/logo/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['-register_date']
