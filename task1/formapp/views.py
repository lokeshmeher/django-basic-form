from django.shortcuts import render
from django.views.generic.edit import CreateView


class HomeView(CreateView):
    model = ShoppingChoice
    template_name = 'formapp/home.html'
