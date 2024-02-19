from django.shortcuts import render, redirect
import logging
from . import forms
from django.conf import settings


logger = logging.getLogger("ex02")


def index(request):
    if request.method == 'POST':
        form = forms.Entry(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['entry'])
        return redirect('index_ex02')
    form = forms.Entry()
    try:
        with open(settings.LOG_FILEPATH, "r") as f:
            history = f.readlines()
    except Exception:
        history = []
    context = {
        'form': form,
        'history': history
    }
    return render(request, 'ex02/index.html', context)
