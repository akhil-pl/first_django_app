from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import Register

# Create your views here.
def  test_view(request):
    return HttpResponse('<h1> This is from blogapp <h1>')

def register_user(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data.get("username"),
                form.cleaned_data.get("email"),
                form.cleaned_data.get("password"),
            )
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return HttpResponse('Thanks')
        
    else:
        form = Register

    return render(request, "register.html", {"form":form})