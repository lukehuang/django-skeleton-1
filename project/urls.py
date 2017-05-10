"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from project import views

from appname import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Uncomment for oauth support
    # url(r'^oauth/', include("oauth.urls")),

    # Auth urls
    url(r'^accounts/login$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/change_password$', views.PasswordChangeView.as_view(), name='change_password'),
    url(r'^accounts/change_password_done$', views.PasswordChangeDoneView.as_view(), name='change_password_done'),

    url(r'', include(urls)),
]
