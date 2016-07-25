from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login

from . import views


app_name = 'formapp'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^create/$', views.CreateChoice.as_view(), name='create'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.RetrieveChoice.as_view(), name='retrieve'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateChoice.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteChoice.as_view(), name='delete'),

    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^register/done/$', views.RegisterDone.as_view(), name='register_done'),
    url(r'^login/$', login, {'template_name': 'formapp/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': 'formapp:login'}, name='logout'),
]
