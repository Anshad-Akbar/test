from django.shortcuts import render

# Create your views here.

def samplefunction(request):
    return render(request,'sample.html')