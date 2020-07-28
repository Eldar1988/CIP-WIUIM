from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import View

from .models import AboutReview, PartnerForms, CompanySocial, Company, QuestionsAbout, Map, Rules, Region
from blog.models import Post


class HomePage(View):
    """Главная страница"""
    def get(self, request):
        user = request.user
        company = Company.objects.first()  # Полная информация о компании
        partner_forms = PartnerForms.objects.all()
        posts = Post.objects.filter(recommend=True)
        reviews = AboutReview.objects.all()  # Отзывы и мнения

        return render(request, 'home/home.html', {
            'company': company,
            'user': user,
            'partner_forms': partner_forms,
            'posts': posts,
            'reviews': reviews,
        })


class AboutUsPage(View):
    """Страница о Нас"""
    def get(self, request):
        company = Company.objects.first()
        questions = QuestionsAbout.objects.all()  # Вопросы и ответы
        reviews = AboutReview.objects.all()  # Отзывы и мнения

        return render(request, 'home/about_us.html', {
            'company': company,
            'questions': questions,
            'reviews': reviews,
        })


class PartnerFormPage(View):
    """Страница формы партнерства"""
    def get(self, request, slug):
        p_form = PartnerForms.objects.get(slug=slug)
        reviews = AboutReview.objects.all()
        return render(request, 'home/partnership.html', {
            'p_form': p_form, 'reviews': reviews
        })


class ContactMap(View):
    """Страница формы партнерства"""
    def get(self, request):
        map = Map.objects.all()
        data = serializers.serialize('json', map)
        return HttpResponse(data, content_type='application/json')


class Faq(View):
    """Вопросы и ответы- страница"""
    def get(self, request):
        questions = QuestionsAbout.objects.all()  # Вопросы и ответы
        return render(request, 'home/faq.html', {
            'questions': questions,
            }
        )


class RulesList(View):
    """Правила Список"""
    def get(self, request):
        return render(request, 'home/rules_list.html')


class RulesPage(View):
    """Правила - страница"""
    def get(self, request, slug):
        rules = Rules.objects.get(slug=slug)  # Вопросы и ответы
        return render(request, 'home/rules.html', {
            'rules': rules,
            }
        )


class ContactPage(View):
    """Страница контактов"""
    def get(self, request):
        company = Company.objects.first()
        socials = CompanySocial.objects.all()
        return render(request, 'home/contacts.html', {
            'company': company,
            'socials': socials,
            }
        )


class MapPage(View):
    """Страница объектов карты"""
    def get(self, request, pk):
        maps = Map.objects.all()

        if pk == 0:
            map = Map.objects.all()
            regions = Region.objects.all()
        else:
            map = Map.objects.filter(region_id=pk)
            regions = Region.objects.filter(id=pk)

        all_regions = Region.objects.all
        paginator = Paginator(map, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        company = Company.objects.first()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        return render(request, 'home/map.html', {
            'maps': maps,
            'page': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'regions': regions,
            'all_regions': all_regions,
            'company': company,
            }
        )


class MapObject(View):
    """Страница объекта карты"""
    def get(self, request, slug):
        map = Map.objects.get(slug=slug)
        x = float(map.x)
        y = float(map.y)
        return render(request, 'home/map_object.html', {
            'map': map,
            'x': x,
            'y': y,
        })








