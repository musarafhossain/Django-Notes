from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayHello(request):
    return render(request,'sayhello/sayhello.html')
