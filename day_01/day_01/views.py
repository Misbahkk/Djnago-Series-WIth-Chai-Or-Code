from django.http import HttpResponse
from django.shortcuts import  render


def home(request):
    return render(request,"index.html")


def about(request):
    # return HttpResponse("Hello, This is  Dajango about page")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("Hello, This is  Dajango contact page")
    return render(request,'contact.html')