from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'main/home_page.html')

def katalog(request):
    return render(request, 'main/katalog.html')