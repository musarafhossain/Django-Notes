from django.shortcuts import render

# Create your views here.

def sayHello(request):
    return render(request, 'sayhello.html')
    
