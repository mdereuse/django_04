from django.shortcuts import render

def django_presentation(request):
    return render(request, 'ex01/django_presentation.html')


def display_presentation(request):
    return render(request, 'ex01/display_presentation.html')


def templates_presentation(request):
    return render(request, 'ex01/templates_presentation.html')
