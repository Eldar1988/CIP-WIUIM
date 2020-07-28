from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_post_count')
    search_fields = ('title',)
    save_as = True

    def get_post_count(self, title):
        posts = Post.objects.filter(category__title=title)
        return posts.count()

    get_post_count.short_description = 'Кол-во постов'



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'post_rating', 'recommend', 'pub_date', 'get_image')
    search_fields = ('title', 'category__title')
    list_filter = ('category', 'author', 'recommend')
    list_editable = ('recommend', 'post_rating', 'category', 'author')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.miniature.url} width="75"')

    get_image.short_description = 'Миниатюра'

    # exclude = ('author',)   # скрыть author поле, чтобы оно не отображалось в форме изменений

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.author = request.user
    #     super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'text', 'parent', 'pub_date')
    search_fields = ('text', 'post__title', 'name')
    list_filter = ('post', 'name')
    readonly_fields = ('parent', 'email', 'name', 'post')


