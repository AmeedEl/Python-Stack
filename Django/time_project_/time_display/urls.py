from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # localhost:8000
    path('time_display/', views.index),   # locatehost:8000/time_display
] 