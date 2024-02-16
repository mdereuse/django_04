from django.shortcuts import render

def index(request):
    color_range =  [
            for i in range(5, 255, 5)
    ]
    context = {
        "color_range": color_range
    }
    return render(request, 'ex03/index.html', context)
