
from django.http import HttpResponse
def index(request):
     return HttpResponse("Home Function </br> <a href='/removefun'>Go to Remove Page</a>")

def removefun(request):
    return HttpResponse("Remove Function</br> <a href='/'>Back to Home</a>")
def NewlineRemovefun(request):
    return HttpResponse("New Line Remove Function/br> <a href='/'>Back to Home</a>")
def Charfun(request):
    return HttpResponse("Char Count Function/br> <a href='/'>Back to Home</a>")
def capFirst(request):
    return HttpResponse("Capitalize Function/br> <a href='/'>Back to Home</a>")

