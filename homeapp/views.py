from django.shortcuts import render


def homeapp(request):
    return render(request, 'index.html')
