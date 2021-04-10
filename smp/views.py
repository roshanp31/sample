
from django.shortcuts import render
def homefun(request):
    return render(request,"home.html")

def helpfun(request):
    
    return render(request,"help.html")    