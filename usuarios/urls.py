from django.urls import re_path
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    re_path(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
    re_path(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='login.html'), name='logout')
]