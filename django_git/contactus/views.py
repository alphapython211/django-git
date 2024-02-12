from django.shortcuts import render,HttpResponse

# Create your views here.

def contactus(request):
    return render(request,'contactus.html')

# def contactus(request):
#     return HttpResponse("hello")