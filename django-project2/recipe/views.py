from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
# Create your views here.

def home(request):
    return render(request, 'recipe/pages/home.html', context={
        'name': 'Matheus Henrique'
    })

