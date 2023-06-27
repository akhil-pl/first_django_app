from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name="blog-home"),
    path('register/', views.register_user, name="register"),
    # path('accounts/', include("django.contrib.auth.urls")), #the html will be checked on "templates/registration folder"
]
