from django.shortcuts import render, redirect

def frontpage(request):
    
    return render(request, 'frontpage.html')

def signin(request):

    return render(request, 'signin.html', context)




