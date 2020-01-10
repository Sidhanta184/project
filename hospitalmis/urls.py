"""hospitalmis URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from.import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^patients/',views.patients,name='patients'),
    url(r'^dashboard/',views.dashboard,name='dashboard'),
    url(r'^login/',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',auth_views.logout,{'next_page':'/login.html/'},name='logout'),
    url(r'^register/',views.register,name='register'),

]