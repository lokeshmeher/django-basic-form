from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'formapp'

urlpatterns = [
    url(r'^$', views.HomePage, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^success/$', views.Success, name='success'),
]
