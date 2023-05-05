from django.shortcuts import render


def home(request):
    return render(request, 'global/home.html', context={
        'name': 'Taciano Levi',
    })
