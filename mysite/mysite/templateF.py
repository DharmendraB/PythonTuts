from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return render(request,'index.html')

def index(request):
    param = {'Name':'Dharmendra Gohil','Place':'Una Gujarat'}
    return render(request,'index.html',param)