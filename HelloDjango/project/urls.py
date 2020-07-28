from django.urls import path
from . import views

urlpatterns = [
    path('add_contact/', views.AddContact.as_view(), name='add_contact'),
    path('', views.ProjectList.as_view(), name='project_list'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('stricture/<slug:slug>/', views.StructureDetail.as_view(), name='structure_detail'),
]