# i have create file-Dharmendra Gohil
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Dharmendra Gohil")

def Aboutus(request):
#Simple Massage retun
# return HttpResponse("Hello Dharmendra Gohil this is AboutUs Function run ")

    #Read Gohil.txt file and open it
    f = open("../Gohil.txt","r")
    contnt = f.read()
    return HttpResponse(contnt)
#Extra Work
def MyfavWebsite(request):
    return HttpResponse("My 1 Favrite Website is= <a href='https://www.facebook.com/ghldharmendra'> My Facebook page</a> </br>My 2 Favrite Website is= <a href='https://www.linkedin.com/in/dharmendraGohil'> My Linkedin page</a>")