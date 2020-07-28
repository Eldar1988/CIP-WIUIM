from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View

from .models import Theme, Comment
from .forms import CommentForm

from contact.models import Bot
import requests


class ThemeList(View):
    """Вывод списка тем"""
    def get(self, request):
        themes = Theme.objects.filter(draft=True)
        paginator = Paginator(themes, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        return render(request, 'forum/theme_list.html', {
            'page': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url})


class ThemeDetail(View):
    """Страница темы"""
    def get(self, request, slug):
        theme = Theme.objects.get(url=slug)
        theme_list = Theme.objects.all()
        body_first_word = theme.body[3]
        body = theme.body[4:]
        comments = Comment.objects.filter(theme__url=slug)
        paginator = Paginator(comments, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        req_user = request.user

        form = CommentForm(request.POST)

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        return render(request, 'forum/theme_detail.html', {
            'page': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'theme': theme,
            'theme_list': theme_list,
            'body_first_word': body_first_word,
            'body': body,
            'form': form,
            'req_user': req_user,
        })


class AddComment(View):
    """Ответ на форуме"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        bot = Bot.objects.get(number=1)

        if form.is_valid():
        #  Отправляем данные в телеграм
            url = f'{bot.url}' + 'sendMessage'
            chat_id = bot.chat_id
            name = request.POST.get('name')  # Поучаем имя пользователя, который оставил сообщение
            title = request.POST.get('title')  # Получаем заголовок страницы
            comment_text = request.POST.get('text')  # Получаем текст сообщения
            comment_url = request.POST.get('url')  # Получаем адрес страницы форума
            text = f'Новое сообщение на форуме \n \n Пользователь: {name} \n ' \
                   f'Тема: {title} \n Сообщение: \n {comment_text} \n \n Адрес: {comment_url}'
            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

            # Сохраняем форму
            form = form.save(commit=False)
            form.theme_id = pk
            if request.POST.get('answer_for', None):
                form.answer_for_id = int(request.POST.get('answer_for'))
            form.save()            


class DelComment(View):

    """Удаление сообщений на форуме"""
    def post(self, request, pk):
        comment_id = int(request.POST.get('id'))
        comment = Comment.objects.get(id=comment_id)

        comment.delete()
        return comment

