from django.urls import path
from . import views
from django.contrib.auth import login

app_name = 'team_project'

urlpatterns = [
    path('captcha', views.send_email_captcha, name='email_captcha'),
    path('login', views.login_view, name='login'),
    # path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
]