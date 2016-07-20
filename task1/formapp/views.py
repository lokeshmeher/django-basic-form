from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import ShoppingChoiceForm, RegisterForm
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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('formapp:register_done'))
    else:
        form = RegisterForm()
    return render(request, 'formapp/register.html', {'form': form})


class RegisterDoneView(TemplateView):
    template_name = 'formapp/register_done.html'
