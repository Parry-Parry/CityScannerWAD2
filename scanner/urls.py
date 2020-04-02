from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from scanner import views

app_name = 'scanner'

urlpatterns = [
  path('locationchoice/', views.locationchoice, name='locationchoice'),
  path('add_nightlife_page/', views.add_nightlife_page, name='add_nightlife_page'),
  path('add_lifestyle_page/', views.add_lifestyle_page, name='add_lifestyle_page'),
  path('add_foodanddrink_page/', views.add_foodanddrink_page, name='add_foodanddrink_page'),
  path('register/', views.register, name='register'),
  path('login/', views.user_login, name='login'),
  path('profile/', views.show_profile, name='profile'),
  path('logout/', views.user_logout, name='logout'),
  path('pagetype/<slug:culture_name_slug>/', views.choose_type, name='choose_type'),
  path('results/nightlife/<slug:culture_name_slug>/', views.show_nightlife, name='show_nightlife'),
  path('results/foodanddrink/<slug:culture_name_slug>/', views.show_foodanddrink, name='show_foodanddrink'),
  path('results/lifestyle/<slug:culture_name_slug>/', views.show_lifestyle, name='show_lifestyle'),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
