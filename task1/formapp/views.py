from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ShoppingChoiceForm
from .models import ShoppingChoice


class HomeView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('formapp:login')
    model = ShoppingChoice
    form_class = ShoppingChoiceForm
    template_name = 'formapp/home.html'
    success_url = reverse_lazy('formapp:success')

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super(HomeView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = 'formapp/success.html'
