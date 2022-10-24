from django.shortcuts import render
from .models import Director, Film


def index(request):
    directors_list = Director.objects.all().order_by('name')
    films = Film.objects.all().order_by('title')

    context = {'directors_list': directors_list,
               'films': films}
    return render(request, 'catalog/index.html', context)


def search(request):
    context = {
    }
    return render(request, 'catalog/search.html', context)


def results(request):

    search = request.POST["name"]
    directors_list = Director.objects.filter(name=search).order_by('name')
    films = Film.objects.all().order_by('title')

    context = {'directors_list': directors_list,
               'films': films,
               'search': search,
               }
    return render(request, 'catalog/results.html', context)
