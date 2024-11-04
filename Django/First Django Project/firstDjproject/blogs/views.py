from django.http import HttpResponse
from django.shortcuts import redirect

def root(request):  # Redirect any request to ( / ) to the /blogs route
    return redirect('/blogs')

def index(request):  # displays a placeholder message for listing blogs
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request): # display a placeholder message for creating a new blog form
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):  # redirect to the root Url ( / ), 
    return redirect('/')    # redirects to the root

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")




