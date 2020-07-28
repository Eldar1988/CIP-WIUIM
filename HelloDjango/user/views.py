from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Profile, Company


class UserDetailView(DetailView):
    model = Profile
    slug_field = 'url'


class CompanyDetailView(DetailView):
    model = Company
    slug_field = 'url'
