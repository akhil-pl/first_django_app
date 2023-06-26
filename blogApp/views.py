from django.shortcuts import render
from django.http import HttpResponse
from .forms import Register

# Create your views here.
def  test_view(request):
    return HttpResponse('<h1> This is from blogapp <h1>')

def register_user(request):
    if request.method == "POST":
        form = Register(request.POST)
    else:
        form = Register

    return render(request, "register.html", {"form":form})