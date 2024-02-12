from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    print("test function call from view")
    return render(request, "about.html")
