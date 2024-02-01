"""
URL configuration for password_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import export_csv, import_csv, suppress_site,change_site,add_site,list_sites, toggle_dark_mode, register
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', list_sites, name='list_sites'),  # URL racine de l'application
    # path('admin/', admin.site.urls),
    path('suppress/<int:site_id>', suppress_site, name='suppress_site'),
    path('change/<int:site_id>', change_site, name='change_site'),
    path('add/', add_site, name='add_site'),
    path('import-csv/', import_csv, name='import_csv'),
    path('export-csv/', export_csv, name='export_csv'),
    path('dark-mode/', toggle_dark_mode, name='toggle_dark_mode'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]