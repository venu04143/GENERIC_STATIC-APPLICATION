from django.shortcuts import render

# Create your views here.


def winter(request):
    return render(request,'winter.html')