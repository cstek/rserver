from django.urls import path
from . import views


urlpatterns = [
    path('rser/', views.temp_here, name='temp_here'),
]