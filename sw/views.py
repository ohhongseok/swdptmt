from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def home(request):
    return render(request, 'index.html')


def introduce(request):
    return render(request, 'swintro.html')


def history(request):
    return render(request, 'swhistory.html')



