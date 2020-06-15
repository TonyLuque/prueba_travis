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
from django.urls import path

def hola(request):
    return HttpResponse('Hola jorge')

urlpatterns = [
    path('colombia/', views_colombia.top_ten),
    path('colombia/department/', views_colombia.top_ten_cities),
    path('colombia/<str:city>', views_colombia.city),
    path('jorge/', hola),

]
