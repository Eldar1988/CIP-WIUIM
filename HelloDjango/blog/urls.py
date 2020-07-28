from django.urls import path
from . import views
# from .views import post_detail, post_list


urlpatterns = [
    path('<slug:slug>', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('del_review/<int:pk>/', views.DelReview.as_view(), name='del_comment'),
    path('category/<slug:slug>/', views.post_list, name='category_detail'),
]