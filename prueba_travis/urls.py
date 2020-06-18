"""prueba_travis URL Configuration

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
from colombia import views as views_colombia
from django.http import HttpResponse 
from django.urls import path
import json

def hola(request,country):
    data = {
        "country_name": country,
        "total_cases": "159,793",
        "active_cases": "21,358",
        "total_deaths": "19,080",
        "new_deaths": "770",
        "total_recovered": "119,355",
        "new_cases": "4,930",
        "serious_critical": "378"
    }
    return HttpResponse(json.dumps(data))

urlpatterns = [
    path('colombia/', views_colombia.top_ten),
    path('colombia/department/', views_colombia.top_ten_cities),
    path('colombia/<str:city>', views_colombia.city),
    path('countries/<str:country>', hola),
]
