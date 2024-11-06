from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the form page.
    path('result/', views.result, name='result'),  # Route for the result page.
]