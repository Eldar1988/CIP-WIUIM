from django import template



from home.models import Company
from home.models import CompanySocial
from home.models import Map
from project.models import Project
from blog.models import Post
from forum.models import Theme
from home.models import Rules
from home.models import Partners
from home.models import PartnerForms

register = template.Library()


@register.simple_tag()
def get_company():
    company = Company.objects.last()
    return company


@register.simple_tag()
def get_social():
    socials = CompanySocial.objects.all()  # Социальные сети
    return socials


@register.simple_tag()
def get_map():
    maps = Map.objects.all()  # Элементы карты
    return maps


@register.simple_tag()
def get_projects():
    projects = Project.objects.all()  # Все проекты
    return projects


@register.simple_tag()
def get_posts():
    posts = Post.objects.all()  # Все посты
    return posts


@register.simple_tag()
def get_themes():
    themes = Theme.objects.all()  # Темы форума
    return themes


@register.simple_tag()
def get_rules():
    rules = Rules.objects.all()  # Вопросы и ответы
    return rules


@register.simple_tag()
def get_partners():
    partners = Partners.objects.all()  # Вопросы и ответы
    return partners


@register.simple_tag()
def get_partner_forms():
    partner_forms = PartnerForms.objects.all()  # Вопросы и ответы
    return partner_forms