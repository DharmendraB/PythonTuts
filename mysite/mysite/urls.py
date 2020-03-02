"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
from . import pip
from . import templateF


#Code for View.py file
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('About', views.Aboutus, name='About'),
#     path('Website',views.MyfavWebsite, name='My Favrite Website' )
# ]
# pip creattion code for pipcreation.py file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', templateF.index, name="index"), # Comment this line For show pip.py file run
    path('', pip.index, name='index'),
    path('removefun', pip.removefun, name='removefun'),
    path('NewlineRemovefun',pip.NewlineRemovefun, name='NewlineRemovefun' ),
    path('Charfun', pip.Charfun, name='Charfun'),
    path('capFirst', pip.capFirst, name='capFirst')
]
