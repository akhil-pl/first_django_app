
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html", {
        'first':10,
        'second':20
    })
    # return HttpResponse("Hello World !!")

def generate(request):
    num = request.GET.get("num")
    upto = request.GET.get("upto")
    return render(request, "table.html", {
        'num':num,
        'upto':upto
    })