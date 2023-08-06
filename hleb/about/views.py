from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

def about(request):
    return render(request, 'about/about.html')

