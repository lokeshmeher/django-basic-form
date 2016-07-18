from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'formapp'

urlpatterns = [
    url(r'^$', views.HomeView, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'formapp/login.html'}, name='login'),
    url(r'^success/$', views.SuccessView, name='success'),
]
