from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')   # render the form page.. 

def result(request):
    if request.method == 'POST':
        # Capture the form data from the POST request..
        name = request.POST.get('name')
        location = request.POST.get('location')
        language = request.POST.get('language')
        comment = request.POST.get('comment')


        # pass the data to the result template..
        context = {
            'name': name, 
            'location': location,
            'language': language,
            'comment': comment
        }
        return render(request, 'result.html', context)
    return redirect('index')   # Redirect to form if not a POST request.