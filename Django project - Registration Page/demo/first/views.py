from django.shortcuts import render
from django.http import HttpResponse
from first.models import Table

# Create your views here.
def home(request):
    if request.method=="POST":
     name=request.POST.get('name')
     Email=request.POST.get('Email')
     course=request.POST.get('course')
     home=Table(name=name,Email=Email,course=course)  
     home.save()
    return render(request,"home.html")
def disp(request):
    return HttpResponse("Hello! from django")