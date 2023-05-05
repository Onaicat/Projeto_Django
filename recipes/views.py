from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'global/home.html', context={
        'name': 'Taciano Levi',
    })


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
