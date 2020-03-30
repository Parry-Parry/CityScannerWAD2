"""CityScanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from scanner import views

app_name = 'scanner'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_nightlife_page/', views.add_nightlife_page, name='add_nightlife_page'),
    path('add_lifestyle_page/', views.add_lifestyle_page, name='add_lifestyle_page'),
    path('add_foodanddrink_page/', views.add_foodanddrink_page, name='add_foodanddrink_page'),
    path('register/', views.register, name='register'),

]
