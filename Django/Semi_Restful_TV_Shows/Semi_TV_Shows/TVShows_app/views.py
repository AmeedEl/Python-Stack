from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def addShow(request):
    return render(request, 'showAdd.html')

def createShow(request):
    errors = Show.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, "showADD.html")
    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], released_date=request.POST['released_date'], desc=request.POST['desc'])
        return redirect(f'/shows/{show.id}')
    
def showID(request, id):
    show = Show.objects.get(id=id)
    request.session['show'] = show.id
    context = {
        "show": show,
    }
    return render(request, 'show_id.html', context)


def deleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

# def edit_show(request, id):
#     show = models.get_show_by_id(id=id)  
#     return render(request, 'showEdit.html', {'show': show})

def edit_show(request, id):
    show = Show.objects.get(id=id)
    context = {
        "show": show,
    }
    if request.method == 'GET':
        request.session['show'] = show.id
        return render(request, 'showEdit.html', context)
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, 'showEdit.html', context)
        else:
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.released_date = request.POST['released_date']
            show.desc = request.POST['desc']
            show.save()
            return render(request, 'shows.html', context)
 
# def update(request, id):
#     if request.method == "POST":
#         Show.update(
#             id=id,
#             title=request.POST['title'],
#             network=request.POST['network'],
#             released_date=request.POST['released_date'],
#             desc=request.POST['desc']
#         )
#         return redirect(f"/shows/{id}")
#     return redirect(f"/shows/{id}/edit")