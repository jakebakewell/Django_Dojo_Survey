from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def result(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['languages']
    comments_from_form = request.POST['comments']
    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "favorite_language_on_template" : language_from_form,
        "comments_on_template" : comments_from_form
    }
    return render(request, 'result.html', context)