from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login

from . import views


app_name = 'formapp'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^register/done/$', views.RegisterDoneView.as_view(), name='register_done'),
    url(r'^login/$', login, {'template_name': 'formapp/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': 'formapp:login'}, name='logout'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
]
