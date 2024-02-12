from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def aboutus(request):
    print("test function call from view")
    return render(request, "aboutus.html")
