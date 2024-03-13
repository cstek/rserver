from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('tt/', views.testMsg, name='testMg'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('attach/', views.attach, name='attach'),
    path('sendToEsp32/', views.sendToEsp32, name='sendToEsp32'),

]