from django.shortcuts import render

# Create your views here.

def chai(request):
    return render(request,'day02_app/chai.html')