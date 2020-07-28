from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project, Data, Benefits, Structure, Questions, Review


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'user', 'order', 'forum_theme', 'get_image', 'pub_date', 'show_count')
    list_editable = ('company', 'user', 'order', 'forum_theme', 'show_count')
    search_fields = ('name',)
    list_filter = ('user', 'company')
    readonly_fields = ('get_image',)
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50"')

    get_image.short_description = 'Картинка'


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_project', 'order', 'number', 'deta_int')
    search_fields = ('name',)
    list_editable = ('number', 'order', 'deta_int')
    save_as = True

    def get_project(self, name):
        project = Project.objects.filter(data__name=name)
        if project.count():
            return project[0]
        else:
            return 'Без проекта'

    get_project.short_description = 'Проект'


@admin.register(Benefits)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_project')
    search_fields = ('title',)
    save_as = True

    def get_project(self, title):
        project = Project.objects.filter(benefits__title=title)
        if project.count():
            return project[0]
        else:
            return 'Без проекта'

    get_project.short_description = 'Проект'


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_project', 'order', 'icon', 'get_image')
    search_fields = ('title',)
    list_editable = ('order',)
    readonly_fields = ('get_image',)
    save_as = True
    save_on_top = True

    def get_project(self, title):
        project = Project.objects.filter(structure_element__title=title)
        if project.count():
            return project[0]
        else:
            return 'Без проекта'

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50"')

    get_project.short_description = 'Проект'
    get_image.short_description = 'Картинка'


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'get_project', 'order')
    search_fields = ('question', 'answer')
    list_editable = ('order',)
    save_as = True

    def get_project(self, question):
        project = Project.objects.filter(questions__question=question)
        if project.count():
            return project[0]
        else:
            return 'Без проекта'

    get_project.short_description = 'Проект'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_project', 'position')
    list_editable = ('position',)
    search_fields = ('name',)
    save_as = True

    def get_project(self, name):
        project = Project.objects.filter(reviews__name=name)
        if project.count():
            return project[0]
        else:
            return 'Без проекта'

    get_project.short_description = 'Проект'


admin.site.site_title = 'Управление сайтом cip wiuim'
admin.site.site_header = 'Управление сайтом cip wiuim'