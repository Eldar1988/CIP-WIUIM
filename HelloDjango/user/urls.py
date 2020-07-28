from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.UserDetailView.as_view(), name='user_detail'),
    path('company/<slug:slug>/', views.CompanyDetailView.as_view(), name='company_detail'),
]