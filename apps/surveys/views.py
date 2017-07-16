from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if 'submissions' not in request.session:
        request.session['submissions'] = 0
    request.session['submissions'] += 1
    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'surveys/result.html')