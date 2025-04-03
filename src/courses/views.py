from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage_view(request):
    return HttpResponse("<h1 style='color:blue;'>Django Course Project.</h1>")
