
from django.shortcuts import render
def homefun(request):
    return render(request,"home.html")

def helpfun(request):
    li=["a","b","c"]
    b=6
    return render(request,"help.html",{'list':li,'value':b})    