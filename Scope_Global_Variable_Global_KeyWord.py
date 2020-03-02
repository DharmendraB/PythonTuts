from django.http import HttpResponse
print("jai mataji")
l = 10 #Global variable

'''
def Function1(n):
   # l = 5 #Local Variable
    m = 8 # Local Variable
    global l
    l = l+1
    print(l,m)
    print(n,"I have printed")
Function1("Hello Gohil")
'''

def Gohil():
    x = 20
    def Ramesh():
        global x
        x =88
    print("Before Calling Ramesh()",x)
    Ramesh()
    print("After Calling Rmaesh()",x)
Gohil()
print(x)


