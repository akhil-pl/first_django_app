
from django.http import HttpResponse
from django.shortcuts import render

from django.template.defaulttags import register


@register.filter
# This is a filter as html has no for loop
def get_range(value):
    return list(range(1, int(value)+1))


def home(request):
    return render(request, "index.html", {
        'first':10,
        'second':20
    })
    # return HttpResponse("Hello World !!")

def generate(request):
    num = request.POST.get("num")
    upto = request.POST.get("upto")
    return render(request, "table.html", {
        'num':num,
        'upto':upto
    })