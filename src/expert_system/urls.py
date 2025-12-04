from django.urls import path
from . import main as views

urlpatterns = [
    path('', views.index, name='index'),
]