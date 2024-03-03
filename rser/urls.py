from django.urls import path
from . import views


urlpatterns = [
    path('tt/', views.testMsg, name='testMg'),
    path('', views.home, name='home'),

]