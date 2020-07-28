from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about_us/', views.AboutUsPage.as_view(), name='about_us'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('partnership/<slug:slug>', views.PartnerFormPage.as_view(), name='partner_forms'),
    path('contacts/', views.ContactPage.as_view(), name='contacts'),
    path('give_map/', views.ContactMap.as_view(), name='give_map'),
    path('rules/', views.RulesList.as_view(), name='rules_all'),
    path('rules/<slug:slug>', views.RulesPage.as_view(), name='rules'),
    path('map/<int:pk>', views.MapPage.as_view(), name='map'),
    path('map/object/<slug:slug>', views.MapObject.as_view(), name='map_object'),
]