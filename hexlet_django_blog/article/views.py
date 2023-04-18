from django.shortcuts import render


def index(request):
    name = 'Article'
    return render(request, 'articles.html', context={'name': name},)