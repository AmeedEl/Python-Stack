from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404
from .models import *
from .forms import *

def dojo_list(request):
    dojos = Dojo.objects.all()
    dojo_form = DojoForm()
    ninja_form = NinjaForm()
    return render(request, 'dojos_list.html', {
        'dojos': dojos,
        'dojo_form': dojo_form,
        'ninja_form': ninja_form
    })


def add_dojo(request):
    if request.method == 'POST':
        dojo_form = DojoForm(request.POST)
        if dojo_form.is_valid():
            dojo_form.save()
    return redirect('dojo_list')
    

def add_ninja(request):
    if request.method == 'POST':
        ninja_form = NinjaForm(request.POST)
        if ninja_form.is_valid():
            ninja_form.save()
    return redirect('dojo_list')


def delete_dojo(request, dojo_id):
    dojo = get_object_or_404(Dojo, id=dojo_id)
    dojo.delete()
    return redirect('dojo_list')
