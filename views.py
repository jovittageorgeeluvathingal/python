from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import product
def home(request):
    return render(request,'index1.html',{'product':product})

def contact(request):
    return HttpResponse(" this is contact page ")

def about(request):
    return HttpResponse("this is about page ")

def index(request):
    product = product.object.all()
    return render(request,'index1.html',{'product':product})

