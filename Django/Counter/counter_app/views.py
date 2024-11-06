from django.shortcuts import render, redirect

# Create your views here.
def root(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    return render(request, 'counter.html')

def destroy_session(request):
    del request.session['visits']
    return redirect('/')