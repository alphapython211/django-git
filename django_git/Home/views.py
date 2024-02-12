from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def navbar(request):
    return render(request,'navbar.html')