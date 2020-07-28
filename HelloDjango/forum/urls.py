from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThemeList.as_view(), name='theme_list'),
    path('<slug:slug>/', views.ThemeDetail.as_view(), name='theme_detail'),
    path('comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('del_comment/<int:pk>/', views.DelComment.as_view(), name='del_comment_forum'),
]