
from django.shortcuts import render
def homefun(request):
    return render(request,"home.html")

def helpfun(request):
    li=["c","d","e"]
    b=7
    return render(request,"help.html",{'list':li,'value':b})    