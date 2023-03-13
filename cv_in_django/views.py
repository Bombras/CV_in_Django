from django.http import HttpResponse
from django.shortcuts import render

def displayPage(request):
    return render(request, 'index.html')