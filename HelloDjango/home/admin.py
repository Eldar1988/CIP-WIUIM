from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Company, PartnerForms, AboutReview, CompanySocial, Map, Region, QuestionsAbout, Rules, Partners


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'email')
    list_editable = ('number', 'email')
    save_on_top = True


@admin.register(PartnerForms)
class PartnerFormsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    save_as = True


@admin.register(AboutReview)
class AboutReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_editable = ('position',)
    save_as = True


@admin.register(CompanySocial)
class CompanySocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_editable = ('url',)
    save_as = True


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'map_title', 'x', 'y', 'region', 'pub_date')
    list_editable = ('map_title', 'x', 'y', 'region')
    list_filter = ('region',)
    save_as = True
    save_on_top = True


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(QuestionsAbout)
class QuestionsAboutAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_editable = ('slug',)
    save_on_top = True


@admin.register(Partners)
class RulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="75"')

    get_image.short_description = 'Логотип'

