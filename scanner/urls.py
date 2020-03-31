from django.urls import path
from scanner import views

app_name = 'scanner'

urlpatterns = [
  path('add_nightlife_page/', views.add_nightlife_page, name='add_nightlife_page'),
  path('add_lifestyle_page/', views.add_lifestyle_page, name='add_lifestyle_page'),
  path('add_foodanddrink_page/', views.add_foodanddrink_page, name='add_foodanddrink_page'),
  path('register/', views.register, name='register'),
  path('login/', views.user_login, name='login'),
  path('profile/', views.show_profile, name='profile'),
  path('logout/', views.user_logout, name='logout'),

  
]
