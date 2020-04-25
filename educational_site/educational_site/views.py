from django.http import HttpResponse
from django.shortcuts import render

def hell_world(request):

    return render(request, 'home.html')