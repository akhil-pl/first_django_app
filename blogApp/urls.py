from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name="test-url"),
    path('test2/', views.test_view2, name="test-url2")
]
