
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html", {
        'first':10,
        'second':20
    })
    # return HttpResponse("Hello World !!")

def generate(request):
    return render(request, "table.html")