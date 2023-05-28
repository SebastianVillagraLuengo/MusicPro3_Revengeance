from django.contrib import admin
from django.urls import path
from .views import home,producto


urlpatterns = [
    path('', home, name='index'),
    path('producto', producto, name='producto'),
]