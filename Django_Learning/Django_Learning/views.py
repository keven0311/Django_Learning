from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! This is home page.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("About page response.")
    return render(request, 'about.html')