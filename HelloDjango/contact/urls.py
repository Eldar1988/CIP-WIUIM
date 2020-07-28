from django.urls import path
from . import views
# from .views import post_detail, post_list


urlpatterns = [
    path('', views.post_list, name='post_list'),
]