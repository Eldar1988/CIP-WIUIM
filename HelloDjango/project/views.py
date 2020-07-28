from django.shortcuts import render
from django.views.generic import View
from .models import Structure, Project

from contact.forms import ContactForm
from contact.models import Bot
from contact.models import Contact

import requests


class ProjectList(View):
    """Вывод списка проектов"""
    def get(self, request):
        projects = Project.objects.filter(draft=True)

        return render(request, 'project/project_list.html', {
            'projects': projects,
            })


class ProjectDetail(View):
    """Страница проекта"""
    def get(self, request, slug):
        project = Project.objects.get(slug=slug)

        return render(request, 'project/project_detail.html', {
            'project': project,
        })


class StructureDetail(View):
    """Элемент структуры проекта"""
    def get(self, request, slug):
        structure = Structure.objects.get(slug=slug)
        project = Project.objects.filter(structure_element__slug=slug)
        project = project.last()

        return render(request, 'project/structure_detail.html', {
            'structure': structure,
            'project': project,
        })


class AddContact(View):
    """Сохранение Контакта"""
    def post(self, request):
        form = ContactForm(request.POST)
        bot = Bot.objects.get(number=1)
        contact = Contact.objects.last()
        if contact and contact.phone == request.POST.get('phone'):
            print('errror')
        if contact and contact.email == request.POST.get('email'):
            print('errror')
        else:
            if form.is_valid():
                #   Отправляем данные в телеграм
                url = f'{bot.url}' + 'sendMessage'
                chat_id = bot.chat_id
                name = request.POST.get('name')  # Поучаем имя
                title = request.POST.get('title')  # Получаем заголовок страницы
                phone = request.POST.get('phone')  # Получаем Телефон

                contact_url = request.POST.get('url')  # Получаем адрес страницы комментария
                text = f'Заявка на обратную связь \n \n Имя: {name} \n ' \
                           f'Телефон: {phone} \n \n Страница: \n {title} \n \n Адрес: {contact_url}'
                if name is None:
                    answer = {'chat_id': chat_id, 'text': 'У нас новый подписчик!'}
                else:
                    answer = {'chat_id': chat_id, 'text': text}
                requests.post(url, answer)

                #   Сохраняем форму
                form.save()

        return form