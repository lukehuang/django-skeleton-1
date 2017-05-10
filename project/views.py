
from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    template_name = 'login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'password_change.html'
    success_url = 'change_password_done'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'password_change_done.html'
