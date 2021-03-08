from django.shortcuts import render

# Create your views here.
def logfunction(request):
    return render(request,'login.html')

def forgetfunction(request):
    return render(request,'forget.html')
    