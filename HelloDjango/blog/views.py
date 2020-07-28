from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View
from django.conf import settings
import requests
from .models import Post, Category, Comment
from .forms import CommentForm
from contact.models import Bot


def post_list(request, slug):
    """Вывод списка постов"""
    if slug == 'all':
        post_list = Post.objects.filter(draft=True)
        bread = '0'
        category = None
    else:
        post_list = Post.objects.filter(draft=True, category__url=slug)
        bread = '1'
        category = Category.objects.get(url=slug)
    paginator = Paginator(post_list, 12)
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

    return render(request, 'blog/post_list.html', {
        'page': page,
        'bread': bread,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'category': category})


def post_detail(request, slug):
    post = Post.objects.get(url=slug)
    post_list = Post.objects.filter(recommend=True)
    body_first_word = post.body[3]
    body = post.body[4:]
    comments = Comment.objects.filter(draft=True, post__url=slug)
    category = Category.objects.all()
    user = request.user
    return render(request, 'blog/post_detail.html',
                  {'post': post,
                   'first_word': body_first_word,
                   'body': body,
                   'comments': comments,
                   'post_list': post_list,
                   'category': category,
                   'user': user})


class AddReview(View):
    """Сохранение Комментариев"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        bot = Bot.objects.get(number=1)

        if form.is_valid():

            #   Отправляем данные в телеграм
            url = f'{bot.url}' + 'sendMessage'
            chat_id = bot.chat_id
            name = request.POST.get('name')  # Поучаем имя пользователя, который оставил комментарий
            title = request.POST.get('title')  # Получаем заголовок страницы
            comment_text = request.POST.get('text')  # Получаем текст комментария
            comment_url = request.POST.get('url')  # Получаем адрес страницы комментария
            text = f'Новый комментарий на сайте \n \n Пользователь: {name} \n ' \
                   f'Пост: {title} \n \n Комментарий: \n {comment_text} \n \n Адрес: {comment_url}'
            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

            #   Сохраняем форму
            form = form.save(commit=False)
            form.post_id = pk

            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))

            form.save()

        return render(request, 'blog/post_detail.html', {'form': form})


class DelReview(View):

    """Удаление комментариев"""
    def post(self, request, pk):
        comment_id = int(request.POST.get('id'))
        comment = Comment.objects.get(id=comment_id)

        comment.delete()
        return comment
