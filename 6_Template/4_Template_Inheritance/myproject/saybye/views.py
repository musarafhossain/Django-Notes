from django.shortcuts import render

# Create your views here.

def sayBye(request):
    return render(request,'saybye/saybye.html')
