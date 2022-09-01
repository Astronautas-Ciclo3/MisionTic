"""RegistraduriaNacional URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from TramitesCedula import views as TramitesCedula


urlpatterns = [
    path('admin/', admin.site.urls),
    path('PrimeraVez/',TramitesCedula.PrimeraVez, name='PrimeraVez'), 
    path('Reexpedicion/',TramitesCedula.Reexpedicion, name='vista1'),
    path('CorrecionDeDatos/',TramitesCedula.correcionDeDatos, name='CorrecionDeDatos'),
    path('cambioDeSexo/',TramitesCedula.cambioDeSexo, name='cambioDeSexo'),

]
