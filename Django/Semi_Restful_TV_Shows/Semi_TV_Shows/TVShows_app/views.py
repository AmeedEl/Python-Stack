from django.shortcuts import render, redirect
from . import models   
from .models import Show


def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        'shows': models.get_all_shows()
    }
    return render(request, "shows.html", context)

def addShow(request):
    return render(request, 'showAdd.html')

def createShow(request):
    models.create_show(request.POST)
    return redirect('/shows') 

    
def showID(request, id):
    context = {
        'show': models.get_show_by_id(id)
    }
    return render(request, 'show_id.html', context)


def deleteShow(request, id):
    models.delete_show(id)
    return redirect('/shows')

def edit_show(request, id):
    show = models.get_show_by_id(id=id)  
    return render(request, 'showEdit.html', {'show': show})

 
def update(request, id):
    if request.method == "POST":
        models.update(
            id=id,
            title=request.POST['title'],
            network=request.POST['network'],
            released_date=request.POST['released_date'],
            desc=request.POST['desc']
        )
        return redirect(f"/shows/{id}")
    return redirect(f"/shows/{id}/edit")