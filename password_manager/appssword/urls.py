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
from .views import suppress_site,change_site,add_site,list_sites

urlpatterns = [
    path('', list_sites, name='list_sites'),  # URL racine de l'application
    # path('admin/', admin.site.urls),
    path('suppress/<int:site_id>', suppress_site, name='suppress_site'),
    path('change/<int:site_id>', change_site, name='change_site'),
    path('add/<int:site_id>', add_site, name='add_site'),
]