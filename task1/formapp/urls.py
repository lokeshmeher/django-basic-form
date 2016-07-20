from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login

from .views import HomeView, SuccessView


app_name = 'formapp'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'formapp/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': 'formapp:login'}, name='logout'),
    url(r'^success/$', SuccessView.as_view(), name='success'),
]
