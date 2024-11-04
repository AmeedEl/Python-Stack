from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # maps to /blogs
    path('new/', views.new, name='new'),  # maps to /blogs/new
    path('create/', views.create, name='create'),  # maps to /blogs/create
    path('<int:number>/', views.show, name='show'),  # maps to /blogs/<number>
    path('<int:number>/edit/', views.destroy, name='destroy'), # maps to /blogs/<number>/delete
   # path('json/', views.json_response, name='json'),  # maps to /blogs/json
]

