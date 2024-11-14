from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addShow),
    path('shows/create', views.createShow),
    path('shows/<int:id>', views.showID),
    path('shows/<int:id>/destroy', views.deleteShow, name='delete_show'),
    path('shows/<int:id>/edit', views.edit_show, name='edit_show'),
    path('shows/<int:id>/update', views.update, name='update')  
]
