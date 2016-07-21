from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import ShoppingChoiceForm, RegisterForm
from .models import ShoppingChoice


class Home(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('formapp:login')
    template_name = 'formapp/home.html'

    def get_queryset(self):
        return ShoppingChoice.objects.filter(submitted_by=self.request.user)


class CreateForm(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('formapp:login')
    model = ShoppingChoice
    form_class = ShoppingChoiceForm
    # template_name = 'formapp/home.html'
    success_url = reverse_lazy('formapp:home')

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super(HomeView, self).form_valid(form)


# class ShowForm(LoginRequiredMixin, DetailView):
#     login_url = reverse_lazy('formapp:login')
#     model = ShoppingChoice
#     template_name = 'formapp/home.html'


class UpdateForm(LoginRequiredMixin, UpdateView):
    # login_url = reverse_lazy('formapp:login')
    # model = ShoppingChoice
    # form_class = ShoppingChoiceForm
    # template_name = 'formapp/home.html'
    pass


# class DeleteForm(LoginRequiredMixin, DeleteView):
#     login_url = reverse_lazy('formapp:login')
#     model = ShoppingChoice


class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'formapp/register.html'
    success_url = reverse_lazy('formapp:register_done')


class RegisterDone(TemplateView):
    template_name = 'formapp/register_done.html'


# class SuccessView(TemplateView):
#     template_name = 'formapp/success.html'
