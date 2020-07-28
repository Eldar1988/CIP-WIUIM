from django.contrib import admin
from .models import Theme, Comment
from project.models import Project


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_project', 'author', 'like', 'pub_date')
    list_editable = ('author', 'like')
    search_fields = ('author', 'title')
    list_filter = ('author',)

    def get_project(self, title):
        project = Project.objects.filter(forum_theme__title=title)
        if project.count():
            return project[0]
        else:
            return 'Без проекта'

    get_project.short_description = 'Проект'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'text', 'answer_for', 'like', 'pub_date')
    search_fields = ('theme__title', 'text')
    list_filter = ('name', 'theme')

