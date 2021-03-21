from django.shortcuts import render
from django.views import generic
from .models import blog


class blogListView(generic.ListView):
    model = blog
    template_name = "home.html"
