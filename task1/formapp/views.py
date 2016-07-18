from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .forms import ShoppingChoiceForm


class HomeView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('formapp:login')
    form_class = ShoppingChoiceForm
    template_name = 'formapp/home.html'


class SuccessView(TemplateView):
    template_name = 'formapp/success.html'
